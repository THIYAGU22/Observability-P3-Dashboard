from flask import Flask, render_template, request, jsonify

import pymongo
import os 

from flask_pymongo import PyMongo

from prometheus_flask_exporter import PrometheusMetrics 
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

trace.set_tracer_provider(
    TracerProvider(
        resource=Resource.create({
            SERVICE_NAME: "backend-service"
        })
    )
)

jaegar_exporter = JaegerExporter()

span_processor = BatchSpanProcessor(jaegar_exporter)

trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)
app = Flask(__name__)

FlaskInstrumentor().instrument_app(app, excluded_urls="metrics")

is_gunicorn = "gunicorn" in os.environ.get("SERVICE_SOFTWARE","")

if(is_gunicorn):
    metrics = GunicornInternalPrometheusMetrics(app)
else:
    metrics = PrometheusMetrics(app)

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)

@app.route('/')
def homepage():
    return "Hello World"


@app.route('/api')
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == "__main__":
    app.run()

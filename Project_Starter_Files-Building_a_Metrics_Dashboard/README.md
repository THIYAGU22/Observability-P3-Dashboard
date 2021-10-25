**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for the three components. Copy and paste the output or take a screenshot of the output and include it here to verify the installation

* Monitoring-namespace-resources:
![Monitoring-namespace-resources](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/monitoring-ns-resources.png?raw=true)

* Default-namespace-resources
![Default-namespace-resources](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/default-ns-resources.png?raw=true)

* Observability-namespace-resources
![Observability-namespace-resources](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/observability-ns-resources.png?raw=true)

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

* Prometheus and Jaeger as a data source 
![Prometheus and Jaeger as a data source](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-datasources.png?raw=true)


## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

* Prometheus Metrics - Monitoring namsespace 
![Prometheus Metrics - Monitoring namsespace ](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/prometheusMetrics-monitoring.png?raw=true)

* Prometheus Metrics - Observability namsespace - Jaeger
![Prometheus Metrics - observability](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/prometheusMetrics-observability-pods.png?raw=true)
 

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

* SLI is a metric to measure the performance at service level. These metrics will be given to customer as a by product.

* Service Level Objective is Service level agreement that is finalised b/w service provider and customer. Measuring the performance of service provider could be uptime of instance should be 99% in a month/ time frame basis. In our case Backend Service should be in service for atleast 99% time. 

* Service latency should be less than 30 ms and consistenly improving the performance of all service calls
  

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

* Uptime -- Service in operate status / available / in-use status. 

* Latency -- Delivery timeframe to generate a response upon requests triggered.

* Traffic -- Huge number of whale requests / stress applied to specific service

* Errors -- Exceptional requests ( example 404 - 4X and 500 - 5X errors)

* Saturation -- Resource consumption by specifc service

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

* SLI - Custom dashboard 
![custom dashboard - 1](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-final-dashboard.png?raw=true)

![custom dashboard - 2](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-final-dashboard1.png?raw=true)

![custom dashboard - 3](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-final-dashboard2.png?raw=true)

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

* Jaeger - Backend Trace - 1 
![Jaeger - Backend Trace - 1](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-backend-trace.png?raw=true)

* Jaeger - Backend Trace - 2
![Jaeger - Backend Trace - 2](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-trace-2.png?raw=true)

* Jaeger - Backend Trace - 3
![Jaeger - Backend Trace - 3](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-backend-trace.png?raw=true)

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

* Jaeger in grafana 
![Jaeger in grafana](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/jaeger-grafana.png?raw=true)

## PromQL 
* PromQL - Jaeger 
 ![PromQL - Jaeger](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/promql2-jaeger.png?raw=true)

* PromQL - Successful request in backend
 ![Successful request](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/promql2-successful-req.png?raw=true)

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name: Backend Service - /star method -HTTP 500

Date: 10/24/2021

Subject: [Backend APP] MONGODB - Resource Unavailable

Affected Area: Backend Service 

Severity: CRITICAL 

Description: Path /star api indicates a mongodb resource which doesnt exists.


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

* Uptime should be guranteed to service at 99 %
* Error rate should be minimalised thereby stabilising success response rate over 99% 
* Service latency : All the api requests should take less than 30ms for each spans


## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

1. Error Rate 
   * Number of errors / sec 
   * Error Response rate / sec 
 
2. Uptime 
   * containers Uptime shld be > 99%
   
3. Service latency 
   * Service latency should be less than 30 ms 
   * Success response rate shld be > 99%
   * Error response rate <= 0.1%
   
4. Resource Consumption 
   * CPU usage by container (Pod) 
   * memory usage by container (Pod) 
   * CPU utilization by container (Pod) 
   * memory utilization by container (Pod) 


## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  

 ![Grafana-Dashboard-1](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-final-dashboard.png)

![Grafana-Dashboard-2](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-final-dashboard1.png)

![Grafana-Dashboard-3](https://github.com/THIYAGU22/Observability-P3-Dashboard/blob/main/Project_Starter_Files-Building_a_Metrics_Dashboard/answer-img/grafana-final-dashboard2.png?raw=true)

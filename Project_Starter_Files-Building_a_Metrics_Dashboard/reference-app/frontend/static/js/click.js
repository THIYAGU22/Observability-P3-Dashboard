$(document).ready(function () {
  // all custom jQuery will go here
  $("#firstbutton").click(function () {
    $.ajax({
      // http://backend.default.svc.cluster.local
      url: "http://localhost:8080",
      success: function (result) {
        $("#firstbutton").toggleClass("btn-primary:focus");
      },
    });
  });
  $("#secondbutton").click(function () {
    $.ajax({
      url: "http://trial.default.svc.cluster.local",
      success: function (result) {
        $("#secondbutton").toggleClass("btn-primary:focus");
      },
    });
  });
});

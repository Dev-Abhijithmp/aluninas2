async function jobViewAction(value) {
    var post = document.getElementById("jobpost").value;
    var description = document.getElementById("jobdescription").value;
    alert(post + "::" + description);
    var jobvi = {}
    jobvi = await $.get("/job/select", { "jobpost": post, "jobdescription": description }, function (data, status, xhr) {
        // console.log("Data: " + data + "\nStatus: " + status);
        return data;
    }, "json");
    alert(json.stringify(job));
    if (job.status === "success") {
        alert("success");
        window.location = "/participate";
    }
    else {
        alert("fail");
        window.location = "/job.html";
    }
}
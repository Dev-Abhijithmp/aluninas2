

function getBaseUrl() {
    return "http://localhost:3001/"
}
// async function loginAction(value) {
//     var usr = document.getElementById("username").value;
//     var pass = document.getElementById("password").value;
//     //alert(usr + "::" + pass);
//     var out = {}
//     // out = await sendAjaxPost("/login", { "username": usr, "password": pass }, "json");
//     out = await $.post("/login", { "username": usr, "password": pass }, function (data, status, xhr) {
//         alert("Data: " + data + "\nStatus: " + status);
//         return data;
//     }, "json");
//     alert(out);
//     if (out.status === "success") {
//         alert("success");
//         window.location = "/home.html";
//     }
//     else {
//         alert("fail");
//         window.location = "/login.html";
//     }

// }

// async function registerAction(value) {
//     alert();
//     var name = document.getElementById("name").value;
//     var pas = document.getElementById("pass").value;
//     var emal = document.getElementById("email").value;
//     var phone = document.getElementById("phone").value;
//     var dob = document.getElementById("dob").value;
//     var gender = document.getElementById("male").value;
//     var gen = document.getElementById("female").value;
//     var gend = document.getElementById("other").value;
//     var retypepass = document.getElementById("repass").value;
//     var age = document.getElementById("age").value;
//     //alert();
//     //alert(name + "::" + pas + "::" + emal + "::" + phone + "::" + dob + "::" + gender + "::" + retypepass + "::" + age);
//     var reg = {}
//     //reg = await sendAjaxPost("/user", { "name": name, "pass": pas, "email": emal, "phone": phone, "dob": dob, "gender": gender, "repass": retypepass, "age": age }, "json");
//     reg = await $.post("/user", { "name": name, "pass": pas, "email": emal, "phone": phone, "dob": dob, "male": gender, "female": gen, "other": gend, "repass": retypepass, "age": age }, function (data, status, xhr) {
//         alert("Data: " + data + "\nStatus: " + status);
//         return data;
//     }, "json");
//     alert(reg);
//     if (reg.status === "success") {
//         alert("success");
//         window.location = "/login.html";
//     }
//     else {
//         alert("fail");
//         window.location = "/registration.html";
//     }

// }

// async function jobAction(value) {

//     var post = document.getElementById("jobpost").value;
//     var description = document.getElementById("jobdescription").value;
//     //alert(post + "::" + description);
//     var job = {}
//     job = await $.Post("/job", { "jobpost": post, "jobdescription": description }, function (data, status, xhr) {
//         alert("Data: " + data + "\nStatus: " + status);
//         return data;
//     }, "json");
//     alert(job);
//     if (job.status === "success") {
//         alert("success");
//         window.location = "/participate";
//     }
//     else {
//         alert("fail");
//         window.location = "/job.html";
//     }
// }
// async function jobViewAction(value) {
//     var post = document.getElementById("jobpost").value;
//     var description = document.getElementById("jobdescription").value;
//     alert(post + "::" + description);
//     var jobvi = {}
//     jobvi = await $.get("/job/select", { "jobpost": post, "jobdescription": description }, function (data, status, xhr) {
//         // console.log("Data: " + data + "\nStatus: " + status);
//         return data;
//     }, "json");
//     alert(json.stringify(job));
//     if (job.status === "success") {
//         alert("success");
//         window.location = "/participate";
//     }
//     else {
//         alert("fail");
//         window.location = "/job.html";
//     }
// }
// async function eventAction(value) {
//     var evtn = document.getElementById("eventname").value;
//     var evtdt = document.getElementById("eventdate").value;
//     var venu = document.getElementById("eventvenue").value;
//     var evttm = document.getElementById("eventtime").value;
//     // alert(evtn + "::" + evtdt + "::" + venu + "::" + evttm);
//     var evet = {}
//     evet = await $.Post("/event", { "eventname": evtn, "eventdate": evtdt, "eventvenue": venu, "eventtime": evttm }, function (data, status, xhr) {
//         alert("Data: " + data + "\nStatus: " + status);
//         return data;
//     }, "json");
//     alert(evet);
//     if (evet.status === "success") {
//         alert("success");
//         window.location = "/";
//     }
//     else {
//         alert("fail");
//         window.location = "/event.html";
//     }
// }

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
function registerAction() {
  var name = document.getElementById("name").value;
  var pass = document.getElementById("pass").value;
  var email = document.getElementById("email").value;
  var phone = document.getElementById("phone").value;
  var dob = document.getElementById("dob").value;
  var radios = document.getElementsByName("gender");
  var course = document.getElementById("course").value;
  var letters = /^[A-Za-z]+$/;
  var nameRegex = /^(?!-)(?!.*-$)[a-zA-Z-]+$/;
  var gend = 0;
  for (var radio of radios) {
    if (radio.checked) {
      gend = 1;
    }
  }

  if (
    name == "" ||
    pass == "" ||
    email == "" ||
    phone == "" ||
    dob == "" ||
    gend == 0 ||
    course == ""
  ) {
    alert("enter all data");
    return false;
  } else {
    if (name.match(letters)) {
        function dateDiffInDays(a, b) {
            const _MS_PER_DAY = 1000 * 60 * 60 * 24;
            // Discard the time and time-zone information.
            const utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
            const utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());
    
            return Math.floor((utc2 - utc1) / _MS_PER_DAY);
          }
    
          // test it
          const a = new Date(Date.now()),
            b = new Date(dob),
            difference = dateDiffInDays(a, b);
    
          console.log(difference + " days");
          if (difference >= 0) {
            alert("enter valid date");
            return false;
          } else {
            return true;
          }
        
    } else {
        alert('Enter valid name')
        
    }
    
      
    
  }
}

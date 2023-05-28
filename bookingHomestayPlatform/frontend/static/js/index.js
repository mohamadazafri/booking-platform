function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays*24*60*60*1000));
  let expires = "expires="+ d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
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

function checkCookie() {
  let username = getCookie("username");
  if (username != "") {
   alert("Welcome again " + username);
  } else {
    username = prompt("Please enter your name:", "");
    if (username != "" && username != null) {
      setCookie("username", username, 365);
    }
  }
}

function getCSRFTokenValue() {
  let element = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  console.log(element)
  return element;
}

function getTodayDate() {

    var date = new Date()
    var day = date.getDate()
    var month = date.getMonth() + 1
    if (month > 12) {month = 1}
    var year = date.getFullYear()

    var uday = day.toString().padStart(2, '0');
    var umonth = month.toString().padStart(2, '0');

    const today = year + "-" + umonth + "-" + uday

    return today
}
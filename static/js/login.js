document.addEventListener("DOMContentLoaded", function() {

    var checkPassword = function(str)
    {
      var re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/;
      return re.test(str);
    };

    var checkForm = function(e)
    {
      if(this.loginPassword.value != "") {
        if(!checkPassword(this.loginPassword.value)) {
          alert("The password you have entered is not valid!");
          this.loginPassword.focus();
          e.preventDefault();
          return;
        }
      }
    };

    var myForm = document.getElementById("loginForm");
    myForm.addEventListener("submit", checkForm, true);

    var supports_input_validity = function()
    {
      var i = document.createElement("input");
      return "setCustomValidity" in i;
    }

    if(supports_input_validity()) {

      var pwd1Input = document.getElementById("loginPassword");
      pwd1Input.setCustomValidity(pwd1Input.title);

      pwd1Input.addEventListener("keyup", function(e) {
        this.setCustomValidity(this.validity.patternMismatch ? pwd1Input.title : "");
      }, false);
    }
  }, false);

function loginValidation(){
  var email = document.forms["loginForm"]["emailId"].value;
  var email_patt = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  /*var password =  document.forms["loginForm"]["loginPassword"].value;
  var passwordpattern=/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;*/

	if(email_patt.test(email) == false )
	{
        document.getElementById('emailAlert').innerHTML=" **Please enter valid Email";
		return false;
	}
	else{
        document.getElementById('emailAlert').innerHTML = '';
		document.getElementById('emailAlert').style.display = 'none';
    }
    /*
    if (passwordpattern.test(password) == false)
    {
        document.getElementById('passwordAlert').innerHTML=" **Please enter valid Password";
		return false;
    }
    else{
        document.getElementById('passwordAlert').innerHTML = '';
		document.getElementById('passwordAlert').style.display = 'none';
    }*/
}

function submitForm(){
    alert("1");
    console.log(document.getElementById("loginForm"));
}
function userQuestion(){
    var loginForm = document.getElementById('main-login-form-section');
    var forgotPasswordForm = document.getElementById('main-forgot-pass-section');
    var loginLi = document.getElementById('login-li');
    loginLi.className="nav-item";
    loginLi.className="underlinehover";
    loginForm.style.display = "none";
    forgotPasswordForm.style.display = "block";
}


function loginValidation(){
    
  var email = document.forms["loginForm"]["emailId"].value;
  var email_patt = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var password =  document.forms["loginForm"]["loginPassword"].value;
  var passwordpattern=/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;

	if(email_patt.test(email) == false )
	{
		document.getElementById('emailAlert').innerHTML=" **Please enter valid Email"
		return false;
	}
	else{
		document.getElementById('emailAlert').innerHTML = '';
		document.getElementById('emailAlert').style.display = 'none';
    }

    if (passwordpattern.test(password) == false)
    {
        document.getElementById('passwordAlert').innerHTML=" **Please enter valid Password"
		return false;
    }
    else{
        document.getElementById('passwordAlert').innerHTML = '';
		document.getElementById('passwordAlert').style.display = 'none';
    }
}

function nameValidation(){
    var email=document.forms["forgetPasswordForm"]["emailId"].value;
    var email_patt=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  
    var q1 = document.forms["forgetPasswordForm"]["question1"].value;
    var q2 = document.forms["forgetPasswordForm"]["question2"].value;
    var q3 = document.forms["forgetPasswordForm"]["question3"].value;
  
      if(email_patt.test(email) == false )
      
          {
              document.getElementById('emailAlert2').innerHTML=" **Please enter valid Email"
              return false;
          }
      else{
          document.getElementById('emailAlert2').innerHTML = '';
          document.getElementById('emailAlert2').style.display = 'none';
      }
   
    var alertMessage = document.getElementById('alert-message');
    var ErrorAlertMessage = document.getElementById('error-alert-message');
    var BlankAlertMessage = document.getElementById('blank-alert-message');

    if (q1 == "" && q2 == "" && q3 == "")
    {
        ErrorAlertMessage.style.display = "none";
        alertMessage.style.display = "none";
        BlankAlertMessage.style.display = "block";
        return false;

    } 
    else if (q1 != "" && q2 == ""  && q3 == "" ||  q1 == "" && q2 != ""  && q3 == "" ||  q1 == "" && q2 == ""  && q3 != ""){
        ErrorAlertMessage.style.display = "block";
        alertMessage.style.display = "none";
        BlankAlertMessage.style.display = "none";
        console.log('In here -2')
        return false;

    }
    else if(q1 != "" && q2 != "" && q3 != "" ) 
    {
        ErrorAlertMessage.style.display = "block";
        alertMessage.style.display = "none";
        BlankAlertMessage.style.display = "none";
        return false;


    }
    else if (q1 != "" && q2 != "" && q3=="" || q1 ==""  && q2 != "" && q3 != "" || q1 != "" && q2== "" && q3 != "")
    {
        var loginForm = document.getElementById('main-login-form-section');
        loginForm.style.display = "none";
        window.location.assign("ResetPassword.html");
        
        
    } 
    return false
}


function ResetFormValidation()
{
    var email=document.forms["ResetPasswordForm"]["emailId"].value;
    var email_patt=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    var password =  document.forms["ResetPasswordForm"]["Resetpassword"].value;
    var passwordpattern=/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
       
    var main_pass=document.forms["ResetPasswordForm"]["Resetpassword"].value;
    var confirm_pass=document.forms["ResetPasswordForm"]["confirmPassword"].value;
    
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

    if(main_pass != confirm_pass)
	{
        document.getElementById('confPasswordAlert').innerHTML='**Please enter the correct Password';
		return false;
	}	
	else{
		document.getElementById('confPasswordAlert').innerHTML = '';
        document.getElementById('confPasswordAlert').style.display = 'none';
	}    
}

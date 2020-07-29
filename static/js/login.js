function loginValidation(){
  var email = document.forms["loginForm"]["emailId"].value;
  var email_patt = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  var password =  document.forms["loginForm"]["loginPassword"].value;
  var passwordpattern=/^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;

	if(email_patt.test(email) == false )
	{
        document.getElementById('emailAlert').innerHTML=" **Please enter valid Email";
		return false;
	}
	else{
        document.getElementById('emailAlert').innerHTML = '';
		document.getElementById('emailAlert').style.display = 'none';
    }

    if (passwordpattern.test(password) == false)
    {
        document.getElementById('passwordAlert').innerHTML=" **Please enter valid Password";
		return false;
    }
    else{
        document.getElementById('passwordAlert').innerHTML = '';
		document.getElementById('passwordAlert').style.display = 'none';
    }
}

function submitForm(){
    alert("1");
    console.log(document.getElementById("loginForm"));
}
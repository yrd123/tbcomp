
function nameValidation(){
    var email=document.forms["forgetPasswordForm"]["emailId"].value;
    var email_patt=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  
    var q1 = document.forms["forgetPasswordForm"]["question1"].value;
    var q2 = document.forms["forgetPasswordForm"]["question2"].value;
    var q3 = document.forms["forgetPasswordForm"]["question3"].value;
  
      if(email_patt.test(email) == false )
      
          {
              document.getElementById('emailAlert').innerHTML=" **Please enter valid Email"
              return false;
          }
      else{
          document.getElementById('emailAlert').innerHTML = '';
          document.getElementById('emailAlert').style.display = 'none';
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
        return false;

    }
    else if(q1 != "" && q2 != "" && q3 != "" ) 
    {
        ErrorAlertMessage.style.display = "block";
        alertMessage.style.display = "none";
        BlankAlertMessage.style.display = "none";
        return false;
    }

}

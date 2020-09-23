


<!DOCTYPE html>
<style>
  .error {color: #FF0000;}
  </style>

<?php

$nameErr= $passErr = $emailErr = $genderErr = $mobileErr = $yearErr = $dateErr = $subjErr =  "";
$username = $pass = $email = $gen = $feed = $mobile = $year = $date = $subj =   "";


function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
  }
  

if($_SERVER["REQUEST_METHOD"] == "POST"){

    if (empty(trim($_POST["Username"]))) {
      $nameErr = "Name is required";
    
    }
    elseif(!preg_match("/^[a-zA-Z0-9\.]*$/", $_POST["Username"])){
        $nameErr = "Only alphabets, numbers are allowed";
    }
    else {
      $username = test_input($_POST["Username"]);
      $username = filter_var($_POST["Username"], FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_HIGH);
    }

    if(empty(trim($_POST["Password"]))){
      $passErr ="Password Required";
    }elseif(!preg_match("/^[a-zA-Z0-9@\.]*$/", $_POST["Password"])){
      $passErr = "Check Password Input";

    }else{
      $pass = test_input($_POST["Password"]);
      $pass = filter_var($_POST["Password"], FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_HIGH);
    }

    if (empty(trim(($_POST["E-mail"])))) {
        $emailErr = "E-Mail is required";
      
      } else {
        $email = test_input($_POST["E-mail"]);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
          $emailErr = "Invalid email format";
        }

      }

      if(empty(trim($_POST["criteria"]))){
        $subjErr = "Enter Criteria";
      }
        else{
          $subj = test_input($_POST["criteria"]);
        }

      if (empty($_POST["Mobile"])) {
        $mobileErr = "Contact number is required";
      
      }
      elseif (strlen($_POST["Mobile"]) != 10)
      {
        $mobileErr = "should be of 10 digits";
      }
      else {
        $mobile = test_input($_POST["Mobile"]);
      }

      if (empty($_POST["Feedback"])) {
        $feed = "";
      
      } else {
        $feed = test_input($_POST["Feedback"]);
        $feed = filter_var($_POST["Feedback"], FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_HIGH);
      }

      if (empty($_POST["gender"])) {
        $genderErr = "Gender is required";
      
      } else {
        $gen = test_input($_POST["gender"]);
      }

      if (empty($_POST["Date"])) {
        $dateErr = "Date is required";
      
      } else {
        $gen = test_input($_POST["Date"]);
      }
      if (empty($_POST["year"])) {
        $yearErr = "Subject is required";
      
      } else {
        $year = test_input($_POST["year"]);
      }
       
      if(empty($nameErr)&&empty($emailErr) && isset($_COOKIE[$x])){
        header('Location: welcome.php?Username='.$username);
      }

}



?>


<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>All inputs</title>
  </head>
  <body>
    <center>
      <h1>Personal Information</h1>
      <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="POST" style="color: bisque ;  ">
        <fieldset style="width: 50%; height: 100%; background-color: rgb(80, 60, 99)">
          Username: <span class="error">* <?php echo $nameErr;?></span><br><input type="text" name="Username" /> <br /><br />

         Password: <span class="error">* <?php echo $passErr;?></span><br><input type="password" name="Password" /> <br /><br />

          E-mail: <span class="error">* <?php echo $emailErr;?></span><br><input type="email" name="E-mail" /> <br /><br />

          Mobile:
          <span class="error">* <?php echo $mobileErr;?></span><br><input type="number" name="Mobile" /> <br /><br />

          Gender: <span class="error">* <?php echo $genderErr;?></span><br>
          <input type="radio" name="gender" value="male" />Male <br />
          <input type="radio" name="gender" value="female" />Female <br /><br />

          Year: <span class="error">* <?php echo $yearErr;?></span> <br>
          <select name="year">
            <option value="FY">FY</option>
            <option value="SY">SY</option>
            <option value="TY">TY</option>
          </select>
          <br /><br />

          Date:<span class="error">* <?php echo $dateErr;?></span><br>
          <input type="date" name="Date"  /> <br><br>


          Subjects:<span class="error">* <?php echo $subjErr;?></span><br>
          <input type="checkbox" name="criteria" value="PHP" />PHP<br />
          <input type="checkbox" name="criteria1" value="REACT" />REACT<br />
          <input type="checkbox" name="criteria2" value="AI" />AI<br />
          <input type="checkbox" name="criteria3" value="HTML" />HTML<br /><br />

          Feedback:
          <textarea name="Feedback" rows="5" cols="40"></textarea> <br /><br />

          <input type="submit" value="submit" name="submit" /> <br />
        </fieldset>
      </form>
    </center>
    
  </body>
</html>

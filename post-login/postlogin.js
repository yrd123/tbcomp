
  function myFunction1() {
      var btn1 = document.getElementById("btn1");
      var btn2 = document.getElementById("btn2");
      var btn3 = document.getElementById("btn3");
      btn2.style.backgroundImage="url('BECIcon.png')";
      btn2.style.backgroundSize="2.1em 3.1em";
      btn2.style.backgroundRepeat="no-repeat";
      btn2.style.backgroundPosition="center";
      btn2.innerText="";
      btn3.style.backgroundImage="url('ECADIcon.png')";
      btn3.style.backgroundSize="1em 1.4em";
      btn3.style.backgroundRepeat="no-repeat";
      btn3.style.backgroundPosition="center";
      btn3.innerText="";
      btn1.style.backgroundColor="#2d9cc2";
      btn2.style.backgroundColor="white";
      btn3.style.backgroundColor="white";
      btn1.style.backgroundImage="none";
      btn1.style.color="white";
      btn2.style.color="black";
      btn3.style.color="black";
      btn1.style.width="8em";
      btn2.style.width="4em";
      btn3.style.width="4em";
      btn1.innerHTML = "EEEE";
        
}
function myFunction2() {
      var btn1 = document.getElementById("btn1");
      var btn2 = document.getElementById("btn2");
      var btn3 = document.getElementById("btn3");
      btn1.style.backgroundImage="url('EEEEIcon.png')";
      btn1.style.backgroundSize="1em 1.4em";
      btn1.style.backgroundRepeat="no-repeat";
      btn1.style.backgroundPosition="center";
      btn1.innerText="";
      btn3.style.backgroundImage="url('ECADIcon.png')";
      btn3.style.backgroundSize="1em 1.4em";
      btn3.style.backgroundRepeat="no-repeat";
      btn3.style.backgroundPosition="center";
      btn3.innerText="";
      btn2.style.color="white";
      btn1.style.color="black";
      btn3.style.color="black";
      btn2.style.backgroundColor="#2d9cc2";
      btn2.style.width="8em";
      btn1.style.width="4em";
      btn3.style.width="4em";
      btn1.style.backgroundColor="white";
      btn3.style.backgroundColor="white";
      btn2.style.backgroundImage="none";
      btn2.innerHTML = "BEC";
      if (window.matchMedia("(max-width: 432px)").matches) { // If media query matches
      footer.className="page2";
      } 
      else{
            footer.className="footer";
      }
     
}
function myFunction3() {
      var btn1 = document.getElementById("btn1");
      var btn2 = document.getElementById("btn2");
      var btn3 = document.getElementById("btn3");
      btn1.style.backgroundImage="url('EEEEIcon.png')";
      btn1.style.backgroundSize="1em 1.4em";
      btn1.style.backgroundRepeat="no-repeat";
      btn1.style.backgroundPosition="center";
      btn1.innerText="";
      btn2.style.backgroundImage="url('BECIcon.png')";
      btn2.style.backgroundSize="2.1em 3.1em";
      btn2.style.backgroundRepeat="no-repeat";
      btn2.style.backgroundPosition="center";
      btn2.innerText="";
      btn3.style.color="white";
      btn2.style.color="black";
      btn1.style.color="black";
      btn3.style.backgroundColor="#2d9cc2";
      btn1.style.backgroundColor="white";
      btn2.style.backgroundColor="white";
      btn3.style.backgroundImage="none";
      btn3.style.width="8em";
      btn2.style.width="4em";
      btn1.style.width="4em";
      btn3.innerHTML = "ECAD";
     if (window.matchMedia("(max-width: 432px)").matches) { // If media query matches
      footer.className="page3";
  } 
  else{
            footer.className="footer";
      }
}
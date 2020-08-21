//For file upload 1
function readURL1(input) {
   
  if (input.files && input.files[0]) 
  {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('.image-upload-wrap1').hide();
      $('.file-upload-content1').show();
      $('.image-title1').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);
  } 
  else {
    removeUpload1();
  }
}
//For file upload 2
function readURL2(input) {

  if (input.files && input.files[0])
  {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('.image-upload-wrap2').hide();
      $('.file-upload-content2').show();
      $('.image-title2').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);
  } 
  else {
    removeUpload2();
  }
}
//For file upload 3
function readURL3(input) {
  
  if (input.files && input.files[0]) 
  {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('.image-upload-wrap3').hide();
      $('.file-upload-content3').show();
      $('.image-title3').html(input.files[0].name);
    };

    reader.readAsDataURL(input.files[0]);
  } 
  else {
    removeUpload3();
  }
}
//Removing the file upload 1
function removeUpload1() {

  var statusBadge = document.getElementById('status-danger-badge1');
  statusBadge.innerHTML = 'No File Attached';
  statusBadge.className = 'badge badge-pill badge-danger';
  document.getElementById('file-upload-input-doc1').value = '';

  $('.file-upload-content1').hide();
  $('.image-upload-wrap1').show();
  
}
//Removing the file upload 2
function removeUpload2() {

  var statusBadge = document.getElementById('status-danger-badge2');
  statusBadge.innerHTML = 'No File Attached';
  statusBadge.className = 'badge badge-pill badge-danger';
  document.getElementById('file-upload-input-doc2').value = '';

  $('.file-upload-content2').hide();
  $('.image-upload-wrap2').show();
  
}
//Removing the file upload 3
function removeUpload3() {

  var statusBadge = document.getElementById('status-danger-badge3');
  statusBadge.innerHTML = 'No File Attached';
  statusBadge.className = 'badge badge-pill badge-danger';
  document.getElementById('file-upload-input-doc3').value = '';
 
  $('.file-upload-content3').hide();
  $('.image-upload-wrap3').show();
  
}
//For file upload 1
$('.image-upload-wrap1').bind('dragover', function () {
  $('.image-upload-wrap1').addClass('image-dropping');
});
$('.image-upload-wrap1').bind('dragleave', function () {
  $('.image-upload-wrap1').removeClass('image-dropping');
});

//For file upload 2
$('.image-upload-wrap2').bind('dragover', function () {
  $('.image-upload-wrap2').addClass('image-dropping');
});
$('.image-upload-wrap2').bind('dragleave', function () {
  $('.image-upload-wrap2').removeClass('image-dropping');
});

//For file upload 3
$('.image-upload-wrap3').bind('dragover', function () {
  $('.image-upload-wrap3').addClass('image-dropping');
});
$('.image-upload-wrap3').bind('dragleave', function () {
  $('.image-upload-wrap3').removeClass('image-dropping');
});


function checkFileUploadDoc1(){
  changeBadge('file-upload-input-doc1','status-danger-badge1');  
}
function checkFileUploadDoc2(){
  changeBadge('file-upload-input-doc2','status-danger-badge2');
}
function checkFileUploadDoc3(){
  changeBadge('file-upload-input-doc3','status-danger-badge3');
}
//Changes the badge (uploaded or no file attached)
function changeBadge(s1,s2){
  var fileInput = document.getElementById(s1);
  var statusBadge = document.getElementById(s2);
 
  if (fileInput.value == 0){
    statusBadge.innerHTML = 'No File Attached';
    statusBadge.className = 'badge badge-pill badge-danger';
  }
  else if(fileInput.value != 0){
    statusBadge.innerHTML = 'Uploaded';
    statusBadge.className = 'badge badge-pill badge-success';
  }
}
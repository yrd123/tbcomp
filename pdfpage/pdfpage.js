function readURL(input) {
    if (input.files && input.files[0]) {
  
      var reader = new FileReader();
  
      reader.onload = function(e) {
        $('.image-upload-wrap').hide();
  
        $('.file-upload-image').attr('src', e.target.result);
        $('.file-upload-content').show();
  
        $('.image-title').html(input.files[0].name);
      };
  
      reader.readAsDataURL(input.files[0]);
  
    } else {
      removeUpload();
    }
  }
  
  function removeUpload() {

    var statusBadge = document.getElementById('status-danger-badge');
    statusBadge.innerHTML = 'No File Attached';
    statusBadge.className = 'badge badge-pill badge-danger';
    
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
    
  }
  $('.image-upload-wrap').bind('dragover', function () {
          $('.image-upload-wrap').addClass('image-dropping');
      });
      $('.image-upload-wrap').bind('dragleave', function () {
          $('.image-upload-wrap').removeClass('image-dropping');
  });
  /*
  $('input[type="file"]').change(function(){ 
    console.log($(this).length);
    if ($(this).length == 0) {
      $("##status-badge").text("Not uploaded");
    } 
    else {
      $("#status-badge").text("File is added!"); 
    }
  }); 
*/
    function checkFileUpload(){
    var fileInput = document.getElementById('file-upload-input');
    var statusBadge = document.getElementById('status-danger-badge');
    if (fileInput.value == 0){
      statusBadge.innerHTML = 'No File Attached';
      statusBadge.className = 'badge badge-pill badge-danger';
    }
    else if(fileInput.value != 0){
      statusBadge.innerHTML = 'Uploaded';
      statusBadge.className = 'badge badge-pill badge-success';
    }
  }
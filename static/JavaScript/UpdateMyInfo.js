function updateInfo(){

    if(!document.getElementById("oldpassword").value){
        alert("Old train ID is required")
        return;
      }

    if(!document.getElementById("").value){
      alert("train ID is required")
      return;
    }
    if(!document.getElementById("trainColor").value){
      alert("train Color is required")
      return;
    }

      if(!document.getElementById("maxTripTime").value){
        alert("maximum trip time is required")
        return;
      }

    const old_password=document.getElementById("oldPassword").value;
    const new_username=document.getElementById("username").value;
    const new_password=document.getElementById("newPassword").value;
    const confirm_password=document.getElementById("confimrPassword").value;
    const new_email=document.getElementById("newEmail").value;
    
    var newdata = { 'oldPassword' : old_password,'username': new_username, 'newPassword': new_password, 'confimrPassword': confirm_password, 'newEmail': new_email}; // Add all attributes
    var csrftoken = document.cookie.split('csrftoken=')[1];
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
  
  $.ajax({
    data: newdata, // get the form data
    type: 'POST', // GET or POST
    url: '/updatemyinfo',
    // on success
    
    success: function (response) {
      console.log(response)
      if(response.done){
        alert("done");
      }
      else if(!response.is_found){
         alert("Scoped train not found ");
      }
      else if(response.already_exist){
        alert("The new id is already exist please choose another ID ");
     }
    },
    // on error
    error: function (response) {
        // alert the error if any error occured
        alert(response.responseJSON.errors);
        console.log(response.responseJSON.errors)
    }
  })
  ;}
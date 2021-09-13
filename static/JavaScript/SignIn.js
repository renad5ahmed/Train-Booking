function Submit(){
  if(!document.getElementById("username").value){      
    alert("Username is required")
    return;
  }
  if(!document.getElementById("password").value){
    alert("Password is required")
    return;
  }
  const name=document.getElementById("username").value;
  const password=document.getElementById("password").value;
  const admin=document.getElementById("isadmin").checked;

  console.log(admin)
  var user = { 'username': name,'password': password, 'isadmin': admin}; // Add all attributes

  var csrftoken = document.cookie.split('csrftoken=')[1];//zy el cookies, bakhod bs tany goz2 mn elgomla b split
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
         xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});

$.ajax({
  data: user, // get the form data
  type: 'POST', // GET or POST
  url: '/signinuser',
  // on success
  success: function (response) {
    console.log(response)
    if(response.is_found && response.isadmin){
      user.username=response.username
      window.location = "/adminhomepage";
  }
   
  else if(response.is_found && !response.isadmin){
    user.username=response.username
    window.location = "/adminhomepage";
  }

  else{
    alert("Username or password is incorrect please check them and check if you are a user or administrator");
  }
  },
  // on error
  error: function (response) {
      alert("Wrong Username or Password, try again!")
      name.value=" "
      password.value=" "
      alert(admin.value)
      // alert the error if any error occured
      window.location="/signin";
  }
})

}
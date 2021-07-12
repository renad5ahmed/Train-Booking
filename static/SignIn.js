function Submit(){
    if(!document.getElementById("username").value){      
      return;
    }
    if(!document.getElementById("password").value){
      name=" "
      return;
    }
    const name=document.getElementById("username").value;
    const password=document.getElementById("password").value;
    const admin=document.getElementById("isadmin").checked;

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
      if(response.is_found){
        window.location = "/homepage";
    }
    },
    // on error
    error: function (response) {
        alert("Wrong Username or Password, try again!")
        name.value=" "
        password.value=" "
        // alert the error if any error occured
        window.location="/signin";
    }
  })

}

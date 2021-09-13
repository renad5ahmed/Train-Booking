function add(){
    console.log("HEllo")
    if(!document.getElementById("trainID").value){
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
    
    const id=document.getElementById("trainID").value;
    const color=document.getElementById("trainColor").value;
    const time=document.getElementById("maxTripTime").value;
    
    var train = { 'trainID': id, 'trainColor': color, 'maxTripTime': time}; // Add all attributes
    var csrftoken = document.cookie.split('csrftoken=')[1];
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
  
  $.ajax({
    data: train, // get the form data
    type: 'POST', // GET or POST
    url: '/addTrainn',
    // on success
    
    success: function (response) {
      console.log(response)
      if(response.is_taken){
        alert("This train " + id + ' already exists');
      }
      else{
         alert("Train added successfully " + id);
         localStorage.setItem('trainID', id);
         window.location = "/homepage";
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
  
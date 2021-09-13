function search(){
  
    const date=document.getElementById("date").value;
    const source=document.getElementById("source").value;
    const dest = document.getElementById("destination").value;
    const numberOfSeats = document.getElementById("requiredNumberOfSeats").value;
    const time = document.getElementById("time").value;
    
    var list = { 'source': source, 'destination': dest, 'requiredNumberOfSeats': numberOfSeats, 'date': date, 'time': time}; // Add all attributes
    var csrftoken = document.cookie.split('csrftoken=')[1];
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
  
  $.ajax({
    data: trip, // get the form data
    type: 'POST', // GET or POST
    url: '/showlist',
    // on success
    
    success: function (response) {
      //console.log(response)
      if(response.is_taken){
        alert("This trip " + id + ' already exists');
      }
      else if(response.trainExist==false){
        alert("This train " + trainId + ' not found');
      }
      
      else{
         alert("Trip added successfully " + id);
         localStorage.setItem('tripID', id);
         window.location = "/homepage";
      }
    },
    // on error
    error: function (response) {
        // alert the error if any error occured
        alert(response.responseJSON.errors);
        //console.log(response.responseJSON.errors)
    }
  })
  ;}
  
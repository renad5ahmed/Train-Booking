function add(){
    if(!document.getElementById("tripID").value){
      alert("trip ID is required")
      return;
    }
    if(!document.getElementById("source").value){
      alert("source is required")
      return;
    }

      if(!document.getElementById("tripTime").value){
        alert("trip time is required")
        return;
      }
      if(!document.getElementById("destination").value){
        alert("destination is required")
        return;
      }
      if(!document.getElementById("requiredNumberOfSeats").value){
        alert("Required Number Of Seats is required")
        return;
      }
  
        if(!document.getElementById("availableNumberOfSeats").value){
          alert("Available Number Of Seats is required")
          return;
        }

        if(!document.getElementById("trainID").value){
            alert("Train ID is required")
            return;
          }
          if(!document.getElementById("cost").value){
            alert("cost is required")
            return;
          }
          if(!document.getElementById("date").value){
            alert("Date is required")
            return;
          }
          if(!document.getElementById("time").value){
            alert("time is required")
            return;
          }

    const id=document.getElementById("tripID").value;
    const source=document.getElementById("source").value;
    const tripTime=document.getElementById("tripTime").value;
    const dest = document.getElementById("destination").value;
    const numberOfSeats = document.getElementById("requiredNumberOfSeats").value;
    const availableSeats = document.getElementById("availableNumberOfSeats").value;
    const trainId = document.getElementById("trainID").value;
    const cost = document.getElementById("cost").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    
    var trip = { 'tripID': id, 'source': source, 'tripTime': tripTime, 'destination': dest, 'requiredNumberOfSeats': numberOfSeats, 'availableNumberOfSeats': availableSeats, 'trainID': trainId, 'cost': cost, 'date': date, 'time': time}; // Add all attributes
    var csrftoken = document.cookie.split('csrftoken=')[1];
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
           xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  });
  
  $.ajax({
    data: trip, // get the form data
    type: 'POST', // GET or POST
    url: '/addtrip',
    // on success
    
    success: function (response) {
      console.log(response)
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
        console.log(response.responseJSON.errors)
    }
  })
  ;}
  
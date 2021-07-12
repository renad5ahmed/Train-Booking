function submit(){
  if(!document.getElementById("username").value){
    return;
  }
  if(!document.getElementById("email").value){
    return;
  }
  if(!document.getElementById("password").value){
    return;
  }
  if(!document.getElementById("password2").value){
    return;
  }
  const name=document.getElementById("username").value;
  const email=document.getElementById("email").value;
  const password=document.getElementById("password").value;
  const password2= document.getElementById("password2").value;
  const admin=document.getElementById("isadmin").checked;
  console.log(admin)
  
  if(password != password2){
    alert("Confirm password must be the same as password")  ;
    return;
  }
  var user = { 'username': name, 'email': email, 'password': password, 'isadmin': admin}; // Add all attributes
  var csrftoken = document.cookie.split('csrftoken=')[1];
  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
         xhr.setRequestHeader("X-CSRFToken", csrftoken);
  }
});

$.ajax({
  data: user, // get the form data
  type: 'POST', // GET or POST
  url: '/signupuser',
  // on success
  success: function (response) {
    console.log(response)
    if(response.is_taken){
      alert("Username " + name + ' already exists, please try another username');
    }
    else{
       alert("Account created successfully " + name);
       localStorage.setItem('username', name);
       localStorage.setItem('userid', response.userid);
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































/*function validateform(){  
var name=document.form.name.value;  
var password=document.form.password.value;  
  
if (name==null || name==""){  
  alert("Name can't be blank");  
  return false;  
}else if(password.length<6){  
  alert("Password must be at least 6 characters long.");  
  return false;  
  }  
}

class DashboardsView extends View{
private:
public:
      DashboardsView(){}
       get(request){     
        return render(request, "dashboard.html");//render y3ny brg3ha b kol elerrors 
    }
}
class SignUpView(generic.CreateView){
    form_class = signUpForm
    template_name = 'signup.html'//b retrieve el signup web page wldata

    function post(self, request){
         form=signUpForm(request.POST)
         if (form.is_valid()){//y3ny eldata tmam
              x = form.save()//hb3to 3l database w a`save it
              return render(request, 'homepage.html', {'form': form , 'user': x.username, 'user_id': x.id})
            }
         return render(request, 'signup.html', {'form': form})//ha3ed nfs el page zyada gomlt el error
}}*/
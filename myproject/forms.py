from django import forms
from myproject.models import User

class signUpForm(forms.ModelForm):
      class Meta:
       model = User
       fields= ['username', 'password', 'confirm_password', 'email', 'is_admin']
       
      username = forms.CharField(required=True)
      password = forms.CharField(required=True)
      confirm_password = forms.CharField(required=True)
      email = forms.CharField(required=True)

      def clean(self):#self y3ny basht8l 3la nfs el instance object
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")#byt2kd mn el pass hena
        if password1 != password2:
            raise forms.ValidationError("Passwords must be identical.")
        return cleaned_data#dictionary feh el data bl values of el form


class signInForm(forms.Form):
    
    username= forms.CharField(label="Enter first  name",max_length=100, required=True)  
    password = forms.CharField(label="Enter password",required=True)

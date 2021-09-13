from django import forms
from myproject.models import User
from myproject.models import Train
from myproject.models import Trip

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


class addTrainForm(forms.ModelForm):
      class Meta:
       model = Train
       fields= ['trainID', 'trainColor', 'maxTripTime']
       
      trainID = forms.CharField(required=True)
      trainColor = forms.CharField(required=True)
      maxTripTime = forms.IntegerField(required=True)

      def clean(self):#self y3ny basht8l 3la nfs el instance object
        cleaned_data = self.cleaned_data
        return cleaned_data#dictionary feh el data bl values of el form


class updateTrainForm(forms.ModelForm):
      class Meta:
       model = Train
       fields= ['trainID']
       
      trainID = forms.CharField(required=True)
      def clean(self):#self y3ny basht8l 3la nfs el instance object
        cleaned_data = self.cleaned_data
        return cleaned_data#dictionary feh el data bl values of el form

class updateScopedTrainForm(forms.ModelForm):
      class Meta:
       model = Train
       fields= ['trainID','trainColor', 'maxTripTime']
       oldTrainId=forms.CharField(required=True)
       trainID = forms.CharField(required=True)
       trainColor = forms.CharField(required=True)
       maxTripTime = forms.IntegerField(required=True)

       def clean(self):#self y3ny basht8l 3la nfs el instance object
         cleaned_data = self.cleaned_data
         return cleaned_data#dictionary feh el data bl values of el form




class showListForm(forms.ModelForm):
      class Meta:
       model = Trip
       fields= ['date','time', 'source','destination','requiredNumberOfSeats']
       date=forms.CharField()
       time = forms.CharField()
       source = forms.CharField()
       destination = forms.CharField()
       requiredNumberOfSeats=forms.IntegerField()

       def clean(self):#self y3ny basht8l 3la nfs el instance object
         cleaned_data = self.cleaned_data
         return cleaned_data#dictionary feh el data bl values of el form





class updateMyInfoForm(forms.ModelForm):
      class Meta:
        model = User
        fields= ['username', 'password', 'email']     
        username = forms.CharField(required=True)
        oldPassword=forms.CharField(required=True)
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


            
class addTripForm(forms.ModelForm):
      class Meta:
       model = Trip
       fields= ['tripID', 'source', 'tripTime','destination','requiredNumberOfSeats','availableNumberOfSeats','trainID','cost','date','time']
       
      tripID = forms.CharField(required=True)
      source = forms.CharField(required=True)
      tripTime = forms.IntegerField(required=True)
      destination = forms.CharField(required=True)
      requiredNumberOfSeats = forms.IntegerField(required=True)
      availableNumberOfSeats = forms.IntegerField(required=True)
      trainID = forms.CharField(required=True)
      cost = forms.FloatField(required=True)
      date = forms.CharField(required=True)
      time = forms.CharField(required=True)

      def clean(self):#self y3ny basht8l 3la nfs el instance object
        cleaned_data = self.cleaned_data
        return cleaned_data#dictionary feh el data bl values of el form



                   
class updateTripForm(forms.ModelForm):
      class Meta:
       model = Trip
       fields= ['tripID', 'source', 'tripTime','destination','requiredNumberOfSeats','availableNumberOfSeats','trainID','cost','date','time']
      oldTripID = forms.CharField(required=True)
      tripID = forms.CharField(required=True)
      source = forms.CharField(required=True)
      tripTime = forms.IntegerField(required=True)
      destination = forms.CharField(required=True)
      requiredNumberOfSeats = forms.IntegerField(required=True)
      availableNumberOfSeats = forms.IntegerField(required=True)
      trainID = forms.CharField(required=True)
      cost = forms.FloatField(required=True)
      date = forms.CharField(required=True)
      time = forms.CharField(required=True)

      def clean(self):#self y3ny basht8l 3la nfs el instance object
        cleaned_data = self.cleaned_data
        return cleaned_data#dictionary feh el data bl values of el form


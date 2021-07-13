from myproject.forms import signUpForm, signInForm
from django.http import HttpResponse, response
from django.conf import settings
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.backends import RemoteUserBackend

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from myproject.models import User
from django.http import JsonResponse

# post function to create a user account
def signup_user(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    admin = request.POST.get('isadmin', None)
    
    if admin=='false':
        admin=False
    else:
        admin=True
    print("el2ola ahy")
    print(admin)#1
    is_taken =  User.objects.filter(username__iexact=username).exists()# filter returns an array
    response = {# initializing dictionary
        'is_taken': is_taken
    }
    if not is_taken:#new one
        admin= True
        user = User.objects.create(username=username, email=email, password=password,is_admin=admin)
        print(user.is_admin)#2
        request.session['userid'] = user.id # global variable
        response['username'] = user.username
        response['useris'] = user.id
        response['is_admin']=user.is_admin
    return JsonResponse(response)

def signin_user(req):
    username = req.POST.get('username', None)#.get returns one element
    password = req.POST.get('password', None)
    Admin= req.POST.get('isadmin', None)
    response = {}# initializing dictionary
    print(Admin)#3
    if Admin=='false':
        Admin=False
    elif Admin=='true':
        Admin=True    
    print(Admin)#4
    print(User.objects.last().is_admin)
    user = User.objects.filter(username__iexact=username, password__iexact=password,is_admin=Admin)#confirming username& pass
    is_found = user.exists()
    if is_found:
        user = user[0]
        response['username'] = user.username
        response['userid'] = user.id
        response['isadmin']=Admin
        response['is_found']=True
        return JsonResponse(response)
    else:
        response['is_found']=False
        errors = 'User not found, please re-try to login'
        username=" "
        password=" "
        response['error']=errors
        return JsonResponse(response)

def homepage(request):
    username = None
    id = None
    if request.session['userid']:
        user = User.objects.get(id=request.session['userid'])
        username = user.username
        id= user.id
    return render(request, 'homepage.html', { 'user': username, 'user_id': id})

import logging
## Main Dashboard page
class DashboardsView(View):
    def get(self, request):      
        return render(request, "dashboard.html")#render y3ny brg3ha b kol elerrors 

class SignUpView(generic.CreateView):
    form_class = signUpForm
    template_name = 'signup.html'#b retrieve el signup web page wldata

    # def post(self, request):
    #      form=signUpForm(request.POST)
    #      if form.is_valid():#y3ny eldata tmam
    #           x = form.save()#hb3to 3l database w a`save it
    #           return render(request, 'homepage.html', {'form': form , 'user': x.username, 'user_id': x.id})
    #      return render(request, 'signup.html', {'form': form})#ha3ed nfs el page zyada gomlt el error

class SignInView(generic.CreateView):
    form_class = signInForm
    template_name = 'signin.html'#b retrieve el signin web page wldata

    def get(self, request):  
        form = signInForm()  
        return render(request, 'signin.html' ,{'form':form})  
    def post(self, request):
         form=signInForm(request.POST)#bageb eldata
         errors = ''
         user = ''
         user_id = ''
         if form.is_valid():
              username = request.POST.get('username')
              password = request.POST.get('password')
              isadmin = request.POST.get('isadmin')
              user = User.objects.filter(username=username, password=password, isadmin=isadmin)#query of django .filter->where ... get->ex. get the id htrg3 7aga wa7da bs
              if len(user):#first user ever
                  user = user[0]
                  user_id = user.id
                  username = user.username
                  return render(request, 'homepage.html', {'form': form , 'user': username, 'user_id': user_id})
                                   
              else:
                  errors = 'User not found, please re-try to login'
         return render(request, 'signin.html', {'form': form , 'errors':errors, 'user': username, 'user_id': user_id})


    

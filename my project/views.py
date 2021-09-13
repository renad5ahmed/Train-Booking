from myproject.forms import signUpForm, signInForm ,addTrainForm,updateTrainForm,updateScopedTrainForm,updateMyInfoForm,addTripForm,updateTripForm,showListForm
from django.http import HttpResponse, response
from django.conf import settings
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.backends import RemoteUserBackend



from myproject.models import Train
from myproject.models import Trip
from myproject.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


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

def search_Train(request):
    trainID = request.POST.get('scope', None)
    print(trainID)
    response={
    }
    train = Train.objects.filter(trainID__iexact=trainID)#confirming username& pass
    is_found = train.exists()
    print(is_found)
    if is_found:
        train = train[0]
        response['trainID'] = train.trainID
        response['trainColor'] = train.trainColor
        response['maxTripTime'] = train.maxTripTime

        response['is_found']=True
        return JsonResponse(response)
    else:
        response['is_found']=False
        errors = 'User not found, please re-try to login'
        response['error']=errors
        return JsonResponse(response)

def update_Train(request):
    oldTrainId=request.POST.get('oldTrainId', None)
    newTrainID = request.POST.get('trainID', None)
    trainColor = request.POST.get('trainColor', None)
    maxTripTime = request.POST.get('maxTripTime', None)
    print(oldTrainId,newTrainID,trainColor,maxTripTime)
    response = {}# initializing dictionary
    train = Train.objects.filter(trainID__iexact=oldTrainId)
    is_found = train.exists()
    train=train[0]
    print(train.trainID)
    train2=Train.objects.filter(trainID__iexact=newTrainID)
    already_exist=train2.exists()
    if is_found and not already_exist:
        scopedTrain = Train.objects.get(trainID=train.trainID)
        scopedTrain.trainID=newTrainID
        scopedTrain.trainColor=trainColor
        scopedTrain.maxTripTime=maxTripTime
        scopedTrain.save()
        response['is_found']=True
        response['already_exist']=already_exist
        return JsonResponse(response)
    else:
        response['is_found']=False
        errors = 'User not found, please re-try to login'
        username=" "
        password=" "
        response['error']=errors
        return JsonResponse(response)


        
    #def update_Train(request):
    #trainID = request.POST.get('trainID', None)
    #if(Train.objects.filter(trainID__iexact=trainID).exists()):
        #response = True
    #else :
        #response=False
    #return JsonResponse(response)

def add_Train(request):
    trainID = request.POST.get('trainID', None)
    trainColor = request.POST.get('trainColor', None)
    maxTripTime = request.POST.get('maxTripTime', None)
    is_taken = Train.objects.filter(trainID__iexact=trainID).exists()# filter returns an array
    response = {# initializing dictionary
        'is_taken': is_taken
    }
    if not is_taken:#new one
        train = Train.objects.create(trainID=trainID, trainColor=trainColor, maxTripTime=maxTripTime)
        response['trainID'] = train.trainID
        print (response)
    return JsonResponse(response)




    
def add_Trip(request):
    tripID = request.POST.get('tripID', None)
    source = request.POST.get('source', None)
    tripTime = request.POST.get('tripTime', None)
    destination = request.POST.get('destination', None)
    requiredNumberOfSeats = request.POST.get('requiredNumberOfSeats', None)
    availableNumberOfSeats = request.POST.get('availableNumberOfSeats', None)
    trainID = request.POST.get('trainID', None)
    cost = request.POST.get('cost', None)
    date = request.POST.get('date', None)
    time = request.POST.get('time', None)
    is_taken = Trip.objects.filter(tripID__iexact=tripID).exists()# filter returns an array
    trainExist= Train.objects.filter(trainID__iexact=trainID).exists()# filter returns an array
    print("hall el train mawgood?? ")
    print(trainExist)
    response = {# initializing dictionary
        'is_taken': is_taken
    }
    response['trainExist']=trainExist
    if ( (not is_taken) and (trainExist) ):#new one
        train=Train.objects.get(trainID=trainID)
        trip = Trip.objects.create(tripID=tripID, source=source, tripTime=tripTime,destination=destination, requiredNumberOfSeats=requiredNumberOfSeats, availableNumberOfSeats=availableNumberOfSeats, trainID=trainID, cost=cost,Date=date, time=time)
        response['tripID'] = trip.tripID
        print("hi")
        print (response)
    return JsonResponse(response)

def update_Trip(request):
    old_TripID = request.POST.get('oldTripID', None)
    tripID = request.POST.get('tripID', None)
    source = request.POST.get('source', None)
    tripTime = request.POST.get('tripTime', None)
    destination = request.POST.get('destination', None)
    requiredNumberOfSeats = request.POST.get('requiredNumberOfSeats', None)
    availableNumberOfSeats = request.POST.get('availableNumberOfSeats', None)
    trainID = request.POST.get('trainID', None)
    cost = request.POST.get('cost', None)
    date = request.POST.get('date', None)
    time = request.POST.get('time', None)
    is_taken = Trip.objects.filter(tripID__iexact=tripID).exists()# filter returns an array
    trip = Trip.objects.filter(tripID__iexact=old_TripID)# filter returns an array
    is_exist=trip.exists()
    train_exist = Train.objects.filter(trainID__iexact=trainID).exists()
    response = {# initializing dictionary
        'is_taken': is_taken
    }
    response['is_exist']=is_exist
    response['train_exist']=train_exist
    if(is_exist and (not is_taken) and train_exist):
        scopedTrip = Trip.objects.get(tripID=old_TripID)
        scopedTrip.tripID=tripID
        scopedTrip.source=source
        scopedTrip.tripTime=tripTime
        scopedTrip.destination=destination
        scopedTrip.requiredNumberOfSeats=requiredNumberOfSeats
        scopedTrip.availableNumberOfSeats=availableNumberOfSeats
        scopedTrip.trainID=trainID
        scopedTrip.cost=cost
        scopedTrip.date=date
        scopedTrip.time=time
        scopedTrip.save()
        print(scopedTrip.tripID)
        response['done'] = True
        print (response)
    return JsonResponse(response)




def show_List(request):
    date = request.POST.get('date', None)
    time = request.POST.get('time', None)
    source = request.POST.get('source', None)
    destination = request.POST.get('destination', None)
    requiredNumberOfSeats = request.POST.get('requiredNumberOfSeats', None)
    #date_exsist= ()
    #trip
    is_taken = True# filter returns an array
    trip = Trip.objects.filter(date__iexact=date)# filter returns an array
    is_exist=trip.exists()
    #train_exist = Train.objects.filter(trainID__iexact=trainID).exists()
    response = {# initializing dictionary
        'is_taken': is_taken
    }
    #response['is_exist']=is_exist
    #response['train_exist']=train_exist
    if(is_taken and is_exist ):
        scopedTrip = Trip.objects.get(Date=date)
        response['tripID']=scopedTrip.tripID
        response['source']=scopedTrip.source
        response['tripTime']=scopedTrip.tripTime
        response['destination']=scopedTrip.destination
        response['requiredNumberOfSeats']=scopedTrip.requiredNumberOfSeats
        response['availableNumberOfSeats']=scopedTrip.availableNumberOfSeats
        response['trainID']=scopedTrip.trainID
        response['cost']=scopedTrip.cost
        response['date']=scopedTrip.Date
        response['time']=scopedTrip.time
        #print(scopedTrip.tripID)
        #response['done'] = True
        #print (response)
    return JsonResponse(response)




def update_Info(request):
    old_password = request.POST.get('oldPassword', None)
    username = request.POST.get('username', None)
    new_password = request.POST.get('newPassword', None)
    confirm_password = request.POST.get('confirmPassword', None)
    new_email = request.POST.get('newEmail', None)
    is_taken = User.objects.filter(username__iexact=username).exists()# filter returns an array
    response = {# initializing dictionary
        'is_taken': is_taken
    }
    identicalpass=False
    current_username=request.user.username
    current_password=request.user.username
    if(old_password==old_password):
        identicalpass=True


    if not is_takennticalpass and identicalpass:#new one
        user = User.objects.get(username=current_username)
        user.username=username
        user.password=new_password
        user.email=new_email
        user.save()
        response['done'] = True
        print (response)
    return JsonResponse(response)


def adminhomepage(request):
    username = None
    id = None
    if request.session['userid']:
        user = User.objects.get(id=request.session['userid'])
        username = user.username
        id= user.id
        print(user.is_admin)
        print("hello admin")
    return render(request, 'homepage.html', { 'user': username, 'user_id': id})


def userhomepage(request):
    username = None
    id = None
    if request.session['userid']:
        user = User.objects.get(id=request.session['userid'])
        username = user.username
        id= user.id
        print("hello user")
    return render(request, 'update.html', { 'user': username, 'user_id': id})



class HelloView(generic.CreateView):
    form_class=addTripForm
    template_name = 'hello.html'



import logging
## Main Dashboard page
class DashboardsView(View):
    def get(self, request):      
        return render(request, "dashboard.html")#render y3ny brg3ha b kol elerrors 

        

class AddTrainView(generic.CreateView):
    form_class = addTrainForm
    template_name = 'addtrain.html'#b retrieve el signup web page wldata

    
class ShowListView(generic.CreateView):
    form_class = showListForm
    template_name = 'showlistt.html'#b retrieve el signup web page wldata



class AddTripView(generic.CreateView):
    form_class = addTripForm
    template_name = 'addtrip.html'#b retrieve el signup web page wldata



class UpdateScopedTrainView(generic.CreateView):
    form_class = updateScopedTrainForm
    template_name = 'udatescopedtrain.html'#b retrieve el signup web page wldata


class UpdateTripView(generic.CreateView):
    form_class = updateTripForm
    template_name = 'tripmodify.html'#b retrieve el signup web page wldata

class UpdateTrainView(generic.CreateView):
    form_class = updateTrainForm
    template_name = 'updatetrain.html'#b retrieve el signup web page wldata

class UpdateMyInfoView(generic.CreateView):
    form_class = updateMyInfoForm
    template_name = 'updatemyinfo.html'#b retrieve el signup web page wldata


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
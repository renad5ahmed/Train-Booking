"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import DashboardsView, SignUpView, SignInView, signup_user, adminhomepage, signin_user ,AddTrainView , add_Train,UpdateTrainView,search_Train,UpdateScopedTrainView,update_Train,userhomepage,update_Info,UpdateMyInfoView,AddTripView,add_Trip,HelloView,UpdateTripView,update_Trip,ShowListView,show_List
from django.conf.urls import url

app_name = 'Dashboards'

urlpatterns = [
   # path('admin/', admin.site.urls),
    url(r'^$', DashboardsView.as_view()),
    url(r'signupuser', signup_user, name='signup_user'),
    url(r'signinuser', signin_user, name='signin_user'),
    url(r'homepage', adminhomepage, name='adminhomepage'),
    url(r'userhomepage', userhomepage, name='userhomepage'),
    #url(r'hello', hello, name='hello'),
    url(r'addTrainn', add_Train,name='add_Train'),
   # url(r'updateTrain', update_Train,name='update_Train'),
    url(r'searchTrain', search_Train,name='search_Train'),
    url(r'searchTrain', search_Train,name='search_Train'),
    url(r'updatescopedtrain', update_Train,name='update_Train'),
    url(r'updatemyinfo', update_Info,name='update_Info'),
    url(r'addtrip',add_Trip,name='add_Trip' ),
    url(r'updatetrip', update_Trip,name='update_Trip'),
    url(r'showlist', show_List,name='show_List'),

   # url(r'update', update, name='update'),
    url(r'signup', SignUpView.as_view()),
    url(r'signin', SignInView.as_view()),#bzwd hena el html pages
    url(r'addtrain', AddTrainView.as_view()),
    url(r'updatetrain', UpdateTrainView.as_view()),
    url(r'udatescopedtrain', UpdateScopedTrainView.as_view()),
    url(r'updatemyinfo', UpdateMyInfoView.as_view()),
    url(r'addtrip', AddTripView.as_view()),
    url(r'hello', HelloView.as_view()),
    url(r'tripmodify', UpdateTripView.as_view()),
    url(r'showlist', ShowListView.as_view()),
   # url(r'update', UpdateView.as_view()),#bzwd hena el html pages
]

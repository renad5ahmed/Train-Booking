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
from .views import DashboardsView, SignUpView, SignInView, signup_user, homepage, signin_user
from django.conf.urls import url

app_name = 'Dashboards'

urlpatterns = [
   # path('admin/', admin.site.urls),
    
    url(r'^pymat/$', DashboardsView.as_view()),
    url(r'signupuser', signup_user, name='signup_user'),
    url(r'signinuser', signin_user, name='signin_user'),
    url(r'homepage', homepage, name='homepage'),
    url(r'signup', SignUpView.as_view()),
    url(r'signin', SignInView.as_view()),#bzwd hena el html pages
]

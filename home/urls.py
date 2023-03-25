from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from home import views
from home.views import homeview, signupview, registerview, login_request, welcomeview, \
    forgetPassword, changePassword, all_user, logOut
from newWaterBillingSystem import settings

app_name = "home"

urlpatterns = [
    path('', homeview, name='homepage'),
    path('login', login_request, name='login-page'),
    path('register', registerview, name="register"),
    path('welcome', welcomeview, name="welcome"),
    path('forgetpassword', forgetPassword, name="forget-password"),
    path('changepassword/<token>/', changePassword, name="change-password"),
    path('logoout', logOut, name="logout"),
    path('alluser', all_user),


]
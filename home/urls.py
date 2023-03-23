from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from home import views
from home.views import homeview, signupview, registerview, login_request, welcomeview, customer_login_view, \
    forgetPassword, changePassword, all_user, logOut, AdminForgetPassword, AdminChangePassword
from newWaterBillingSystem import settings

app_name = "home"

urlpatterns = [
    path('', homeview, name='homepage'),
    path('login', login_request, name='login-page'),
    path('register', registerview, name="register"),
    path('welcome', welcomeview, name="welcome"),
    path('customer_login', customer_login_view, name='customer_login'),
    path('forgetpassword', forgetPassword, name="forget-password"),
    path('adminforgetpassword', AdminForgetPassword, name="admin-forget-password"),
    path('adminchangepassword', AdminChangePassword, name="admin-change-password"),
    path('logoout', logOut, name="logout"),
    # path('changepassword', changePassword, name="change-password"),
    path('changepassword/<token>/', changePassword, name="change-password"),
    path('alluser', all_user),


]
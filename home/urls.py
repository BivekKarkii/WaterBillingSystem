from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from home import views
from home.views import *
from newWaterBillingSystem import settings

app_name = "home"

urlpatterns = [
    path('', homeview, name='homepage'),
    path('login', login_request, name='login-page'),
    path('register', registerview, name="register"),

    path('edit', editView, name='edit'),
    path('update/<str:id>', updateView, name='update'),
    path('delete/<str:id>', deleteView, name='delete'),

    path('welcome', welcomeview, name="welcome"),
    path('forgetpassword', forgetPassword, name="forget-password"),
    path('changepassword/<token>/', changePassword, name="change-password"),
    path('logoout', logOut, name="logout"),
    path('alluser', consumerView),
    path('about', aboutview, name="about"),
    path('support', supportview, name="support"),
    path('contact', contactview, name="contact"),

    path('employeetable', employeeview, name="employeetable"),
    path('employeeedit', employeeeditView, name='employeeedit'),
    path('employeeupdate/<str:id>', employeeupdateView, name='employeeupdate'),
    path('employeedelete/<str:id>', employeedeleteView, name='employeedelete'),

    path('billview', billview, name="billview"),
    path('viewbill/<str:id>', billView, name='viewbill'),

]
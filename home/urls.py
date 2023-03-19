from django.contrib import admin
from django.urls import path

from home import views
from home.views import homeview, signupview, loginview, registerview, login_request, welcomeview, customer_login_view

app_name = "home"

urlpatterns = [
    path('', homeview, name='homepage'),
    path('login', login_request, name='login-page'),
    path('register', registerview, name="register"),
    path('welcome', welcomeview, name="welcome"),
    path('customer_login', customer_login_view, name='customer_login'),

]
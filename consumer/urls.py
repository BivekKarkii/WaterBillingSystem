from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from consumer.views import customer_login_view
from home import views
from home.views import homeview

app_name = "consumer"

urlpatterns = [
    path('customer_login', customer_login_view, name='customer_login'),


]
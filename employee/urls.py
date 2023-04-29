from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from employee.views import employee_dashboardview, employee_registration_formview

app_name = "employee"

urlpatterns = [
    path('employee_dashboard', employee_dashboardview, name='employee_dashboard'),
    path('employee_registration_form', employee_registration_formview, name='employee_registration_form'),
]
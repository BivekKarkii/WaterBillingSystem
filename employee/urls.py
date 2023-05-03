from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from employee.views import employee_dashboardview, employee_registration_formview, employee_login_view, \
    employeelogoutview

app_name = "employee"

urlpatterns = [
    path('employeelogin', employee_login_view, name='employeelogin'),
    path('employee_dashboard', employee_dashboardview, name='employee_dashboard'),
    path('employee_registration_form', employee_registration_formview, name='employee_registration_form'),
    path('employeelogout', employeelogoutview, name='employeelogout'),


]
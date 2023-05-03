from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random

from billing.models import consumerBilling
from consumer.models import Consumer
from employee.models import Employee, Employee_Profile


# Create your views here.

def employee_dashboardview(request):
    consumer = Consumer.objects.all()
    a = 0

    billing = consumerBilling.objects.all()
    c = 0
    for i in billing:
        c = +1

    for i in consumer:
        a += 1
    context = {
        'consumer': consumer,
        'count': a,
        'billing': billing,
        'countbill': c,
    }
    return render(request, 'employee_dashboard.html',context)

def employee_registration_formview(request):
    if request.method == 'POST':
        employee_id = request.POST.get("employee_id")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        citizenship = request.POST.get("citizenship")
        password = request.POST.get("password")

        print(employee_id)

        Employee.objects.create(
            employee_id=employee_id,
            name=name,
            phone=phone,
            email=email,
            address=address,
            citizenship=citizenship,
            password=password
        )
        # print("user created!")
        return redirect("/employeetable")

    return render(request, "employee_registration_form.html")

def employee_login_view(request):
    if request.method == "POST":
        print("Hello employee")
        phone = request.POST.get('phone')
        password = request.POST.get('Cpassword')

        try:
            usr = Employee.objects.filter(phone=phone, password=password)
            print(usr.first().phone)
            return redirect("/employee/employee_dashboard")

        except:
            print("Whattttttttttttttttt")
            return render(request, "employee_login.html", context={"message": "invalid username or password"})

    form = AuthenticationForm()
    return render(request=request, template_name="employee_login.html", context={"login_form": form})

@login_required
def employeelogoutview(request):
    logout(request)
    return redirect('/employee_login_view')
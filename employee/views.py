from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
import random
from django.views.generic.base import TemplateView

import employee
from billing.models import consumerBilling
from consumer.models import Consumer
from employee.models import Employee, Employee_Profile


# Create your views here.

def employee_dashboardview(request):
    # get the logged in employee's info'
    employee_id = request.session.get('employee_id')

    emp = Employee.objects.filter(employee_id=employee_id)
    print("HEkkkkkkkkkk", emp)


    consumer = Consumer.objects.all()
    a = 0

    billing = consumerBilling.objects.values('consumer_det_id').distinct()
    consumer_billing_list = []
    for consumer_id in billing:
        last_billing = consumerBilling.objects.filter(consumer_det=consumer_id['consumer_det_id']).order_by('-id')
        if last_billing:
            consumer_billing_list.append(last_billing)

    # print("counterrrrr",consumer_billing_list)
    billcounter = consumerBilling.objects.all()
    c = 0

    # for l in consumer_billing_list:
    #     for i in l:
    #         print(i.amount)

    for i in billcounter:
        c = +1
        # print(i.consumer_det.name)
    for i in consumer:
        a += 1
    context = {
        'consumer': consumer,
        'count': a,
        'billing': billcounter,
        'countbill': c,
        'consumer_billing_list':consumer_billing_list,
        'emp':emp,
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
        return redirect("/welcome")

    return render(request, "employee_registration_form.html")



def employee_login_view(request):
    if request.method == "POST":
        print("Hello employee")
        phone = request.POST.get('phone')
        password = request.POST.get('Cpassword')

        try:
            usr = Employee.objects.filter(phone=phone, password=password)
            print(usr.first().phone)
            request.session['employee_id'] = usr.first().employee_id
            print(usr.first().employee_id)
            return redirect("/employee/employee_dashboard")

        except:
            print("Whattttttttttttttttt")
            return render(request, "employee_login.html", context={"message": "invalid username or password"})

    form = AuthenticationForm()
    return render(request=request, template_name="employee_login.html", context={"login_form": form})

# @login_required
# def employeelogoutview(request):
#     logout(request)
#     return redirect('/employee_login_view')


class ConsumerSignedOutView(TemplateView):
    template_name = "employee_login.html"
    def get(self, request: HttpRequest):
        logout(request)
        # return render(request, self.template_name)
        return redirect('/employee/employeelogin')

def deleteView(request, id):
    consumer = Consumer.objects.filter(id=id)
    consumer.delete()

    context = {
        'consumer': consumer,
    }
    return redirect('/welcome')


@login_required
def employeeview(request):
    employee = Employee.objects.all()
    b = 0
    for i in employee:
        b += 1
        print(i)
    context = {
        'employee': employee,
        'count': b
    }
    return render(request, 'admindashboard.html', context)


def employeeeditView(request):
    employee = Employee.objects.all()
    for i in employee:
        print(i.employee_id)
    context = {
        'employee': employee,
    }
    return render(request, 'index.html', context)


def employeeupdateView(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        citizenship = request.POST.get('citizenship')
        employee_id = request.POST.get('employee_id')
        e_password = request.POST.get('password')

        employee = Employee(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
            citizenship=citizenship,
            employee_id=employee_id,
            password=e_password,
        )
        employee.save()
        return redirect('/welcome')
    return render(request, 'index.html')


def employeedeleteView(request, id):
    employee = Employee.objects.filter(id=id)
    employee.delete()

    context = {
        'employee': employee,
    }
    return redirect('/welcome')


def updateView(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        citizenship = request.POST.get('citizenship')
        employee_id = request.POST.get('employee_id')
        password = request.POST.get('password')

        employee = Employee(
            id=id,
            employee_id=employee_id,
            name=name,
            phone=phone,
            email=email,
            address=address,
            citizenship=citizenship,
            password=password,
        )
        employee.save()
        return redirect('/employee/employee_dashboard')
    return render(request, 'employee_dashboard.html')


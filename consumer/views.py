from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
import random
from django.views.generic.base import TemplateView
from consumer.forms import ConsumerForm
from consumer.models import Consumer, Consumer_Profile
from billing.models import consumerBilling


# Create your views here.

def consumer_dashboardview(request):
    billing = consumerBilling.objects.all()
    a=0

    for i in billing:
        a += 1


    context = {
        'count': a,
        'billing': billing,
    }
    return render(request, 'consumer_dashboard.html',context)

def customer_login_view(request):
    if request.method == "POST":
        print("Hello bivek")
        phone = request.POST.get('phone')
        password = request.POST.get('Cpassword')

        try:
            usr=Consumer_Profile.objects.filter(phone=phone, password=password)
            print(usr.first().phone)
            return redirect("/consumer/consumer_dashboard")

        except:
            return render(request, "customer_login.html", context={"message":"invalid username or password"})
        # return render(request, "customer_login.html", context={"message": "invalid username or password"})

    form = AuthenticationForm()
    return render(request=request, template_name="customer_login.html", context={"login_form": form})


def consumer_registration_formview(request):
    if request.method == 'POST':
        consumer_id = request.POST.get("consumer_id")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        meter_no = request.POST.get("meter_no")
        type = request.POST.get("type")
        citizenship = request.POST.get("citizenship")

        print(consumer_id)

        Consumer.objects.create(
            consumer_id=consumer_id,
            name=name,
            phone=phone,
            email=email,
            address=address,
            meter_no=meter_no,
            type=type,
            citizenship=citizenship
        )
        # print("user created!")
        return redirect("/welcome")

    return render(request, "consumer_registration_form.html")

def consumer_adminview(request):
    return render(request, "consumer.html")

def consumer_signupview(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')

        if password!=c_password:
            return render(request, "Signup.html", {"message": "password not matching"})
        # print(f'hellllllllllllloooooooooo{phone}')
        try:
            consum = Consumer.objects.get(phone=phone)
            Consumer_Profile.objects.create(phone=phone, password=password)
            print(consum.phone)
            # Consumer_Profile.save()
            # print(consum.email)
            return redirect('/consumer/customer_login')
        except:
            return render(request, "Signup.html",{"message":"Invalid phone number"})

        # if Consumer.objects.get(consumer_id=cid):
        #     print('Success')
        #     return render(request, "Signup.html")


    return render(request, "Signup.html")

# def consumer_updateview(request, phone):
#     consumer = Consumer.objects.get(phone=phone)
#     form = ConsumerForm(request.POST or None, instance=consumer)
#     if form.is_valid():
#         form.save()
#         return redirect('/consumer/consumer_admin')
#     return render(request, '/consumer/consumer_update_form.html', {'consumer_update_form': form})

# def consumer_delete(request, id):
#     pass
    # consumer = Consumer.objects.get(id=id)
    # if request.method == 'POST':
    #     consumer.delete()
    #     return redirect('consumer_list')
    # return render(request, 'consumer/delete.html', {'consumer': consumer})


# @login_required
# def consumerlogoutview(request):
#     logout(request)
#     return redirect('/customer_login_view')

class SignedOutView(TemplateView):
    template_name = "customer_login.html"
    def get(self, request: HttpRequest):
        logout(request)
        return render(request, self.template_name)
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from consumer.models import Consumer, Consumer_Profile


# Create your views here.

def consumer_dashboardview(request):
    return render(request, 'consumer_dashboard.html')

def customer_login_view(request):
    if request.method == "POST":
        print("Hello gello")
        username = request.POST.get('Cid')
        password = request.POST.get('Cpassword')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.info(request, f"You are now logged in as {username}.")
            return redirect(f"/consumer_dashboard?username={username}")
        else:
            print("no user")
            messages.error(request, "Invalid username or password.")
        # else:
        #     messages.error(request, "Invalid username or password.")
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
        return redirect("/consumer/consumer_admin")

    return render(request, "consumer_registration_form.html")

def consumer_adminview(request):
    return render(request, "consumer.html")

# def consumer_signupview(request):
#     if request.method == 'POST':
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         c_password = request.POST.get('c_password')
#
#         if password!=c_password:
#             return render(request, "Signup.html", {"message": "password not matching"})
#         print(f'hellllllllllllloooooooooo{phone}')
#         try:
#             consum = Consumer.objects.get(phone=phone)
#             Consumer_Profile.objects.create(phone=phone, password=password)
#
#             print(consum.phone)
#             # Consumer_Profile.save()
#
#             # print(consum.email)
#             return redirect('/consumer/customer_login')
#         except:
#             return render(request, "Signup.html",{"message":"Consumer id is invalid"})
#
#         # if Consumer.objects.get(consumer_id=cid):
#         #     print('Success')
#         #     return render(request, "Signup.html")
#
#
#     return render(request, "Signup.html")



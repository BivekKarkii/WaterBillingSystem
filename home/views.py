from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from consumer.models import Consumer
from .helpers import send_forget_password_mail

# from home.forms import UserLoginForm
from .models import Profile
import uuid


# Create your views here.
def homeview(request):
    return render(request, 'index.html')


def signupview(request):
    pass

@login_required
def welcomeview(request):
    consumer = Consumer.objects.all()
    a=0
    for i in consumer:
        a+=1
        # print(a)
    context = {
        'consumer':consumer,
        'count':a
    }
    return render(request, 'admindashboard.html',context)


@login_required
def logOut(request):
    logout(request)
    return redirect('/login')
    # return render(request, 'login.html') #issue 1


def login_request(request):
    if request.method == "POST":
        # print("Hello gello")
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.info(request, f"You are now logged in as {username}.")
            return redirect(f"/welcome?username={username}")
        else:
            print("no user")
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def registerview(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # Validate the input
        if not username or not password:
            return HttpResponse(status=400, content='Username and password are required')

        # Create a new user with the create_user method
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create()
        print("user created!")
        return redirect("/login")

    return render(request, "signup.html")


def changePassword(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.get(forget_password_token=token)
        context = {'user_id': profile_obj.user_id}

        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('c_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'/changePassword/{token}/')

            if new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/changePassword/{token}/')

            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login')

    except Exception as e:
        print(e)

    return render(request, 'change_password.html', context)


# http://127.0.0.1:8000/changepassword/fe930ab0-be5a-433b-b738-82c5bd3d4001/
def forgetPassword(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            print(username)
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('/forgetpassword')

            # print("hello"+username)
            user_obj = User.objects.get(username=username)

            token = str(uuid.uuid4())

            profile_obj = Profile.objects.get(user=user_obj)

            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)

            messages.success(request, 'An email has been sent to your registered email. Please check your mail.')
            return redirect('/forgetpassword')

    except Exception as e:
        print(e)
    return render(request, 'forget_password.html')



def consumerView(request):
    # consumer = Profile.objects.all()
    # print(consumer)
    # context = {
    #     'consumer': consumer
    # }
    # print(context)
    return render(request, 'welcome.html')

def aboutview(request):
    return render(request, 'aboutus.html')

def supportview(request):
    return render(request, 'support.html')

def contactview(request):
    return render(request, 'contactus.html')

def editView(request):
    cons = Profile.objects.all()
    context = {
        'cons':cons,
    }
    return render(request, 'index.html', context)


def updateView(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        meter_no = request.POST.get('meter_no')
        type = request.POST.get('type')
        citizenship = request.POST.get('citizenship')
        consumer_id = request.POST.get('consumer_id')

        cons = Profile(
            id = id,
            name = name,
            email=email,
            address=address,
            phone=phone,
            meter_no=meter_no,
            type=type,
            citizenship=citizenship,
            consumer_id=consumer_id
        )
        cons.save()
        return redirect('/')
    return render(request, 'index.html')


def deleteView(request,id):
    cons = Profile.objects.filter(id=id)
    cons.delete()

    context = {
        'cons': cons,
    }
    return redirect('/')
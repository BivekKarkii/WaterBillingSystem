from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .helpers import send_forget_password_mail

from home.forms import UserLoginForm
from .models import Profile
import uuid


# Create your views here.
def homeview(request):
    return render(request, 'index.html')


def signupview(request):
    pass


# def login_view(request):
#     next = request.GET.get('next')
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect('home:welcome')
#
#     context = {
#         'form': form,
#     }
#     return render(request, "login.html", context)

@login_required
def welcomeview(request):
    return render(request, 'welcome.html')


def customer_login_view(request):
    return render(request, 'customer_login.html')

@login_required
def logOut(request):
    logout(request)
    return render(request, 'login.html')


def login_request(request):
    if request.method == "POST":
        print("Hello gello")
        # form = AuthenticationForm(request, data=request.POST)
        # if form.is_valid():
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect(f"/welcome?username={username}")
        else:
            print("no user")
            messages.error(request, "Invalid username or password.")
        # else:
        #     messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def registerview(request):
    if request.method == 'POST':
        # Extract the username and password from the request body
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        # Validate the input
        if not username or not password:
            return HttpResponse(status=400, content='Username and password are required')

        # Create a new user with the create_user method
        user = User.objects.create_user(username=username, password=password)
        print("user created!")
        return redirect("/login")
        # return HttpResponse(status=201, content='User created')

    return render(request, "signup.html")


def changePassword(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.get(forget_password_token=token).first()
        print(profile_obj)

        context = {'user_id': profile_obj.user_id}
    except Exception as e:
        print(e)
    return render(request, 'change_password.html', context)


# http://127.0.0.1:8000/changepassword/fe930ab0-be5a-433b-b738-82c5bd3d4001/
def forgetPassword(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('/forgetpassword')

            # print("hello"+username)
            user_obj = User.objects.get(username=username)

            token = str(uuid.uuid4())
            print(Profile.objects.all())
            profile_obj = Profile.objects.get(user=user_obj)

            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)

            messages.success(request, 'An email has been sent to your registered email. Please check your mail.')
            return redirect('/forgetpassword')

    except Exception as e:
        print(e)
    return render(request, 'forget_password.html')



def AdminForgetPassword(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('/forgetpassword')

            # print("hello"+username)
            user_obj = get_user_model.objects.get(username=username)
            user_obj.setpassword


    except Exception as e:
        print(e)
    return redirect('/adminchangepassword')

# def adminchangeView(request):
#     return render(request, 'change_password.html')
def AdminChangePassword(request, username):
    try:
        if request.method == "POST":
            password = request.POST.get('password')
            confirm_password = request.POST.get('c_password')

            if (password != confirm_password):
                messages.success(request, 'password mismatch!')
                return redirect('/adminchangepassword')

            UserModel = get_user_model().filter(username=username)
            UserModel.set_password(confirm_password)
            UserModel.save()
            return redirect(request, '/login')


    except Exception as e:
        print(e)
    return render(request, 'change_password.html')



def all_user(request):
    emp = User.objects.all()
    print(emp)
    context = {
        'emp': emp
    }
    print(context)
    return render(request, 'welcome.html', context)

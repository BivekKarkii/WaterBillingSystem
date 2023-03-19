from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def homeview(request):
    return render(request, 'index.html')


def signupview(request):
    pass


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'welcome.html')
        else:
            messages.error(request, "Bad credientials")
            print("login error!")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def welcomeview(request):
    return render(request, 'welcome.html')
def customer_login_view(request):
    return render(request, 'customer_login.html')

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
            return redirect("/welcome")
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


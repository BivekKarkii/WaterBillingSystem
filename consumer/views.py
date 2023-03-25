from django.shortcuts import render

# Create your views here.
def customer_login_view(request):
    return render(request, 'customer_login.html')
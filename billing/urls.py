from django.urls import path
from django.contrib.auth import views as auth_views

from billing.views import meter_readingFormview

app_name = "billing"

urlpatterns = [
    path('meter_readingForm', meter_readingFormview, name='meter_readingForm'),
]
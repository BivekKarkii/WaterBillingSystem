from django import forms
from .models import Consumer

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ('name', 'email', 'phone', 'address')
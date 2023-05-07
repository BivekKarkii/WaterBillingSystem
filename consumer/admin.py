from django.contrib import admin

from consumer.models import Consumer, Consumer_Profile, PasswordProfile

# Register your models here.
admin.site.register(Consumer)
admin.site.register(Consumer_Profile)
admin.site.register(PasswordProfile)
from django.contrib import admin

from billing.models import *


# Register your models here.


# class BillingAdmin(admin.ModelAdmin):
#     ADMIN_SITE_TITLE = ['Consumer Id', 'Name', 'Previous unit', 'Current Unit']


admin.site.register(consumerBilling)

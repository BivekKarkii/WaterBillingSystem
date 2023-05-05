from random import random

from django.db import models

# Create your models here.
class Consumer(models.Model):
    id = models.IntegerField(primary_key=True)
    consumer_id = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    meter_no = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)


    def __str__(self):
        return "%s   %s" % (self.consumer_id, self.name)

class Consumer_Profile(models.Model):
    consumer = models.OneToOneField(Consumer, on_delete=models.CASCADE, null=True)
    #consumer_details = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return "%s's profile" % (self.consumer.name)

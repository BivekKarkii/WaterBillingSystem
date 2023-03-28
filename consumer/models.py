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

    # print(type(id))

    # c_random=0
    # def randomNumber(self):
    #     c_random = random.randint(1000, 9999)
    # print(f"hello {c_random}")
    # consumer_id = c_random

    def __str__(self):
        return "%s   %s" % (self.consumer_id, self.name)

class Consumer_Profile(models.Model):
    # consumerobj = models.OneToOneField(Consumer, on_delete=models.CASCADE)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.consumer} {self.password}"
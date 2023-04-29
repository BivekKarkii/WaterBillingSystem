from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "%s   %s" % (self.employee_id, self.name)

class Employee_Profile(models.Model):
    # consumerobj = models.OneToOneField(Consumer, on_delete=models.CASCADE)
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
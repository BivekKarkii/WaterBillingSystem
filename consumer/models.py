from django.db import models

# Create your models here.
class Consumer(models.Model):
    id = models.IntegerField(primary_key=True, max_length=10)
    consumer_id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    meter_no = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)

    def __str__(self):
        return "%s   %s" % (self.consumer_id, self.name)
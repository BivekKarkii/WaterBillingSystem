from django.db import models

# Create your models here.
class consumerBilling(models.Model):
    id = models.IntegerField(primary_key=True)
    invoice_id = models.IntegerField()
    # employee_id = models.IntegerField()
    consumer_id = models.IntegerField()
    consumer_name = models.CharField(max_length=60)
    previous_unit = models.CharField(max_length=50)
    current_unit = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    meter_number = models.IntegerField()

    def __str__(self):
        return "%s   %s" % (self.consumer_id, self.consumer_name)
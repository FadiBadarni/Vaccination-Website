from django.db import models

# Create your models here.
class appointments(models.Model):
    user_name = models.CharField(max_length=30)
    appointment_time =models.TimeField(max_length=30)

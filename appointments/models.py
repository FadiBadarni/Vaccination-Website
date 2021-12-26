from django.db import models


class Appointment(models.Model):
    user = models.CharField(max_length=50)
    time = models.TimeField(auto_now_add=True)






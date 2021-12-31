from django.db import models
from phone_field import PhoneField


class Doctor(models.Model):
    username = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

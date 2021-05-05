from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contacts (models.Model):
    name = models.CharField(max_length=100 , primary_key=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
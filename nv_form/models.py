from django.db import models

# Create your models here.

class User(models.Model):
    fullname = models.CharField(max_length= 200)
    email_address = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    volunteering_experience = models.CharField(max_length=100)
    member_of_aiesec = models.BooleanField(default=False)
    travel_from = models.CharField(max_length=200,)
    prefer_location = models.CharField(max_length=200)
    preferred_project = models.CharField(max_length=100)
    health_issues = models.BooleanField(default=False)
    please_specify = models.CharField(max_length=200, blank=True)
    who_do_we_contact = models.CharField(max_length=200)
    emergency_contact = models.CharField(max_length=100)
    anything_else_to_know = models.CharField(max_length=200, blank=True)



from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=60)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    place = models.CharField(max_length=70, null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True ,
        blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True,
        blank=True)
    # amount employer is willing to pay per hour
    pay = models.PositiveIntegerField(default=10) 
    employer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
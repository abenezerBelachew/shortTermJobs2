from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=60)
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/', null=True ,
        blank=True)
    # amount employer is willing to pay per hour
    pay = models.PositiveIntegerField(default=10) 
    tags = TaggableManager()

    def __str__(self):
        return self.title
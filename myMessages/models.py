from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyMessage(models.Model):
    id = models.AutoField(primary_key = True)       
    subject = models.CharField(max_length = 50)
    body = models.CharField(max_length = 250) 
    isActive = models.BooleanField()
    datePosted = models.DateTimeField(auto_now_add=True) 
    postedBy = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
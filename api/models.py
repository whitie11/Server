from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ROLE_CHOICE =[('SuperUser','Super User'), ('StdUser', 'Standard User')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICE, default = 'Standard User')

class Staff(models.Model):
    staffId = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length = 10)
    lastName = models.CharField(max_length = 15)
    userName = models.CharField(max_length = 26)
    grade = models.IntegerField()
    initials = models.CharField(max_length = 3)

    def __str__(self):
        return self.userName

    

class Duty(models.Model):
    dutyId = models.AutoField(primary_key = True)
    dutyType = models.CharField(max_length = 50)   
    dutyCode = models.CharField(max_length = 2) 

    def __str__(self):
        return self.dutyType

class Alloc(models.Model):
    SESSION_CHOICE =[('AM','morning'), ('PM', 'afternoon')]

    allocId = models.AutoField(primary_key = True)
    date = models.DateField()
    session = models.CharField(max_length = 2, choices = SESSION_CHOICE, default = 'morning')
    duty = models.ForeignKey(Duty, null = True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null = True, on_delete=models.SET_NULL)

    class Meta:
        unique_together =('date', 'session', 'staff')

class ToDo(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 50) 
    isCompleted = models.BooleanField()  
    title = models.CharField(max_length = 50) 

# class Message(models.Model):
#     id = models.AutoField(primary_key = True)       
#     subject = models.CharField(max_length = 50)
#     body = models.CharField() 
#     isActive = models.BooleanField()
#     datePosted = models.DateField(auto_now=True) 
#     postedBy = models.ForeignKey(User, on_delete=models.SET_NULL)
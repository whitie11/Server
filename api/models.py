from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    ROLE_CHOICE = [('SuperUser', 'Super User'),
                   ('StdUser', 'Standard User'), ('Guest', 'Guest')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICE, default='Guest')

    def __str__(self):
        return str(self.user)


class Staff(models.Model):
    staffId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=15)
    userName = models.CharField(max_length=26, unique=True)
    grade = models.IntegerField()
    initials = models.CharField(max_length=3)

    def __str__(self):
        return self.userName


class Duty(models.Model):
    dutyId = models.AutoField(primary_key=True)
    dutyType = models.CharField(max_length=50)
    dutyCode = models.CharField(max_length=2)
    sortIndex = models.DecimalField(
        max_digits=6, decimal_places=2, default=1.0)

    def __str__(self):
        return self.dutyType


class Alloc(models.Model):
    SESSION_CHOICE = [('AM', 'morning'), ('PM', 'afternoon')]

    allocId = models.AutoField(primary_key=True)
    date = models.DateField()
    session = models.CharField(
        max_length=2, choices=SESSION_CHOICE, default='AM')
    duty = models.ForeignKey(Duty, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    savedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    class Meta:
        unique_together = ('date', 'session', 'staff')

    def __str__(self):
        return (str(self.date) + ' ' + self.session + ' ' + str(self.staff))

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.allocId:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Alloc, self).save(*args, **kwargs)


class AllocLog(models.Model):
    allocLogId = models.AutoField(primary_key=True)
    allocId = models.IntegerField()
    date = models.DateField()
    session = models.CharField(max_length=2)
    duty = models.ForeignKey(Duty, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    savedBy = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def __str__(self):
        return (str(self.date) + ' ' + self.session + ' ' + str(self.staff))





class ToDo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    isCompleted = models.BooleanField()
    title = models.CharField(max_length=50)

# class Message(models.Model):
#     id = models.AutoField(primary_key = True)
#     subject = models.CharField(max_length = 50)
#     body = models.CharField()
#     isActive = models.BooleanField()
#     datePosted = models.DateField(auto_now=True)
#     postedBy = models.ForeignKey(User, on_delete=models.SET_NULL)

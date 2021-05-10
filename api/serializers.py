from rest_framework import serializers
from api.models import Alloc, Duty, Profile, Staff, ToDo
from django.contrib.auth.models import User

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('staffId', 'firstName', 'lastName', 'userName', 'grade', 'initials')

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = ('dutyId', 'dutyType', 'dutyCode')

class AllocSerializer(serializers.ModelSerializer):
    duty = DutySerializer()
    staff = StaffSerializer()
    
    class Meta:
        model = Alloc
        fields = ('allocId', 'date', 'session', 'duty', 'staff', 'savedBy', 'created', 'modified')
    
class AllocPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alloc
        fields = ('allocId', 'date', 'session', 'duty', 'staff', 'savedBy')

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('title', 'isCompleted')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'role', 'user_id', 'staff_id') 



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    # staff = StaffSerializer()
    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'is_staff', 'is_active', 'is_superuser', 'profile')


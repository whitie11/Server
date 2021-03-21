
from rest_framework import serializers
from django.contrib.auth.models import User
from myMessages.models import MyMessage
from api.models import Duty, Staff
from rostaApp.models import Config


class StaffSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Staff
        fields = ('__all__')

class DutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Duty
        fields = ('dutyId', 'dutyType', 'dutyCode')        

class RotaSerializer(serializers.ModelSerializer):
    staff = StaffSerializer()
    dutyArray = DutySerializer()
    class Meta:
        model = MyMessage
        fields = ('id', 'subject', 'body', 'isActive', 'datePosted', 'postedBy')    

class ConfigSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Config
        fields = ('__all__')        
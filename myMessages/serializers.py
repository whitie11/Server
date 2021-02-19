
from rest_framework import serializers
from django.contrib.auth.models import User
from myMessages.models import MyMessage

class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class MyMessageSerializer(serializers.ModelSerializer):
    postedBy = UserSerializer()
    class Meta:
        model = MyMessage
        fields = ('id', 'subject', 'body', 'isActive', 'datePosted', 'postedBy')        

class MyMessagePostSerializer(serializers.ModelSerializer):
    postedBy = UserSerializer(read_only=True)
    postedBy_id = serializers.IntegerField(write_only= True)
    class Meta:
        model = MyMessage
        fields = ( '__all__')

from django.shortcuts import get_object_or_404, render
from .serializers import MyMessageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse, JsonResponse
from myMessages.models import MyMessage
from rest_framework.parsers import JSONParser
from myMessages.serializers import MyMessagePostSerializer
import datetime



@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the mymessages index.")
    
@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def all_messages(request):
    if request.method == 'GET':
        messages_all = MyMessage.objects.all()
        serialiser = MyMessageSerializer(messages_all, many=True)
        return JsonResponse(serialiser.data, safe=False)
    return JsonResponse(serialiser.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def archive_message(request):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        id = data['id']
        message_to_update = get_object_or_404(MyMessage, pk=id)
        message_to_update.isActive = False
        message_to_update.save()
        serialiser = MyMessageSerializer(message_to_update, many=False)
        return JsonResponse(serialiser.data, safe=False)
    return JsonResponse(serialiser.errors, status=400)   

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def all_messages_from_date(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        date_from = data['postedStr']
        date_obj = datetime.datetime.strptime(date_from, '%m/%d/%Y')
        messages_from_date = MyMessage.objects.filter(datePosted__gt=date_obj)
        serialiser = MyMessageSerializer(messages_from_date, many=True)
        return JsonResponse(serialiser.data, safe=False)
    return JsonResponse(serialiser.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def filtered_messages_from_date(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        x = data['postedStr']
        date_time_obj = datetime.datetime.strptime(x, '%m/%d/%Y')
        if data['incArchived'] == True:
           messages_from_date = MyMessage.objects.filter(datePosted__gt=date_time_obj )
        else: 
           messages_from_date = MyMessage.objects.filter(datePosted__gt=date_time_obj, isActive=True)
        serialiser = MyMessageSerializer(messages_from_date, many=True)
        return JsonResponse(serialiser.data, safe=False)
    return JsonResponse(serialiser.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serialiser = MyMessagePostSerializer(data=data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status=400)
    return JsonResponse(serialiser.errors, status=400)
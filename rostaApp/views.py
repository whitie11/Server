from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from api.models import Alloc
from datetime import timedelta
from django.http import HttpResponse

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def duties_from_date(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        date_from = data['weekStartStr']
        date_start = datetime.datetime.strptime(date_from, '%m/%d/%Y')
        date_end = date_start + timedelta(days=14)
        staffArr = data['staffList']
        savedDuties = Alloc.objects.filter(date__range=(date_start, date_end))
        print(savedDuties)
        rota = []
        for staff in staffArr:
         rotaRow = []
         rotaRow.append(staff)
         test_date = date_start
         while test_date < date_end:
            duty = next((x.duty for x in savedDuties if (
                x.staff_id == staff and x.date== test_date.date() and x.session == 'AM')), None)
            if duty:
             rotaRow.append(duty)
            else:
             rotaRow.append(None)
             
            duty = next((x.duty for x in savedDuties if (
                x.staff_id == staff and x.date== test_date.date() and x.session == 'PM')), None)
            if duty:
             rotaRow.append(duty)
            else:
             rotaRow.append(None)
            test_date += timedelta(days=1)
         rota.append(rotaRow)
        # next staff
        x = rota
        return HttpResponse("Hello, world. You're at duties from date.")
          #   
#         messages_from_date = MyMessage.objects.filter(datePosted__gt=date_obj)
#         serialiser = MyMessageSerializer(messages_from_date, many=True)
#         return JsonResponse(serialiser.data, safe=False)
#     return JsonResponse(serialiser.errors, status=400)

from django.shortcuts import render
from rest_framework.parsers import JSONParser
import datetime

# Create your views here.

# @api_view(['POST'])
# @permission_classes([IsAuthenticated]) 
# @csrf_exempt
# def duties_from_date(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         date_from = data['weekStartStr']
#         date_obj = datetime.datetime.strptime(date_from, '%m/%d/%Y')
#         staffArr = data['staffList']
          # get Alloc from date_obj to (date_obj + 14 days)

          # new Rota
            # for each staff in staffArr
                # new rota row
                # push staff
                # for each date_obj to (date_obj + 14 days) get Alloc where date & staff
                 # if Alloc push to rotarow
                 # else push empty duty
                # next day
            #push rotarow to rota
            # next staff 
          #   
#         messages_from_date = MyMessage.objects.filter(datePosted__gt=date_obj)
#         serialiser = MyMessageSerializer(messages_from_date, many=True)
#         return JsonResponse(serialiser.data, safe=False)
#     return JsonResponse(serialiser.errors, status=400)

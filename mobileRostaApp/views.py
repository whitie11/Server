from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import dateutil
from datetime import timedelta
from api.models import Alloc, Duty, Staff
import json
from django.http import HttpResponse
from django.db.models import Model
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.

class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)
        return super().default(o)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def myduties_from_date(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        date_from = data['weekStartStr']
        date_start = dateutil.parser.isoparse(date_from)
        date_end = date_start + timedelta(days=5)
        staffId = data['staffId']
        savedDuties = Alloc.objects.filter(date__range=(date_start, date_end))
        rotaArray = []
        test_date = date_start
        # loop through 7 days
        # foreach savedDuty test for day and shift
        # if staff = staffId set rotaArray Duty
        # then if duty = Duty(not unavailabilites!) add staff initials to others
        dayNo = 0 
        day_name= ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat','Sun']
        while test_date < date_end:
            
            shiftRow = {
                'day': '',
                'duty': '',
                'others': ''
            }

            shiftRow['day'] = day_name[dayNo] + ' AM'
            
            duty = next((x.duty for x in savedDuties if (
                x.staff_id == staffId  and x.date == test_date.date() and x.session == 'AM')), None)
            if duty:
                shiftRow['duty'] = duty.dutyType
                # check for others
                if (duty.sortIndex < 90): 
                    qs1 = savedDuties.filter(date = test_date.date(), session = 'AM', duty = duty.dutyId).exclude(staff = staffId)
                    if qs1:
                        others = ''
                        for s in qs1:
                            others = others + ' ' + s.staff.initials + ','
                        shiftRow['others'] = others
                else:
                    shiftRow['others'] ='***'        

            else:
                shiftRow['duty'] = '?'   
                

            rotaArray.append(shiftRow) 
            
            shiftRow = {
                'day': '',
                'duty': '',
                'others': ''
            }

            shiftRow['day'] = day_name[dayNo] + ' PM'

            duty1 = next((x.duty for x in savedDuties if (
                x.staff_id == staffId  and x.date == test_date.date() and x.session == 'PM')), None)
            if duty1:
                shiftRow['duty'] = duty1.dutyType
                # check for others
                if (duty1.sortIndex < 90): 
                    qs1 = savedDuties.filter(date = test_date.date(), session = 'PM', duty = duty1.dutyId).exclude(staff = staffId)
                    if qs1:
                        others = ''
                        for s in qs1:
                            others = others + ' ' + s.staff.initials + ','
                        shiftRow['others'] = others
                else:
                    shiftRow['others'] ='***'        
            else:
                shiftRow['duty'] = '?'   
                
            rotaArray.append(shiftRow)

            dayNo += 1
            test_date += timedelta(days=1)
        # next staff
        
        x = list(rotaArray)

        res = json.dumps(x, cls=ExtendedEncoder)

        return HttpResponse(res, content_type="application/json")


           
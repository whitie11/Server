from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import datetime
from api.models import Alloc, Duty, Staff
from datetime import timedelta
from django.http import HttpResponse, JsonResponse
import json
from json import JSONEncoder
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from api.serializers import DutySerializer
import dateutil.parser

# Create your views here.


class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, Model):
            return model_to_dict(o)

        return super().default(o)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def get_duties(request):
    if request.method == 'GET':
        duties = Duty.objects.all()
        serialiser = DutySerializer(duties, many=True)
        return JsonResponse(serialiser.data, safe=False)
    return JsonResponse(serialiser.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def duties_from_date(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        date_from = data['weekStartStr']
        date_start = dateutil.parser.isoparse(date_from)
        date_end = date_start + timedelta(days=14)
        staffArr = data['staffList']
        savedDuties = Alloc.objects.filter(date__range=(date_start, date_end))
        rotaArray = []

        for staff in staffArr:
            rotaRow = []
            s = Staff.objects.get(pk=staff)
            rotaRow.append(s)
            dutyRow = []
            test_date = date_start

            while test_date < date_end:
                duty = next((x.duty for x in savedDuties if (
                    x.staff_id == staff and x.date == test_date.date() and x.session == 'AM')), None)
                if duty:
                    dutyRow.append(duty)
                else:
                    dutyRow.append(None)

                duty1 = next((x.duty for x in savedDuties if (
                    x.staff_id == staff and x.date == test_date.date() and x.session == 'PM')), None)
                if duty1:
                    dutyRow.append(duty1)
                else:
                    dutyRow.append(None)

                test_date += timedelta(days=1)

            rotaRow.append(dutyRow)
            # dutyRow = []
            rotaArray.append(rotaRow)

        # next staff
        x = list(rotaArray)

        res = json.dumps(x, cls=ExtendedEncoder)

        return HttpResponse(res, content_type="application/json")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt
def duty_staff_from_date(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        date_from = data['weekStartStr']
        date_start = dateutil.parser.isoparse(date_from)
        date_end = date_start + timedelta(days=14)
        dutyIdArr = data['dutyIdArray']
        savedDuties = Alloc.objects.filter(date__range=(date_start, date_end))
        rotaArray_duty = []

        for dutyId in dutyIdArr:
            rotaRow = []
            duty = Duty.objects.get(pk=dutyId)
            rotaRow.append(duty)
            staffRow = []
            test_date = date_start

            while test_date < date_end:
                filteredAlloc = savedDuties.filter(duty_id=dutyId).filter(
                    date=test_date.date()).filter(session='AM')
                if filteredAlloc:
                    staffArray = []
                    for a in filteredAlloc:
                        staff = Staff.objects.get(pk=a.staff_id)
                        staffArray.append(staff)
                    staffRow.append(staffArray)
                else:
                    staffRow.append(None)

                filteredAlloc = savedDuties.filter(duty_id=dutyId).filter(
                    date=test_date.date()).filter(session='PM')
                if filteredAlloc:
                    staffArray = []
                    for a in filteredAlloc:
                        staff = Staff.objects.get(pk=a.staff_id)
                        staffArray.append(staff)
                    staffRow.append(staffArray)
                else:
                    staffRow.append(None)

                test_date += timedelta(days=1)

            rotaRow.append(staffRow)
            rotaArray_duty.append(rotaRow)

        # next staff
        x = list(rotaArray_duty)

        res = json.dumps(x, cls=ExtendedEncoder)

        return HttpResponse(res, content_type="application/json")

from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from .models import Staff, Duty, Alloc
from .serializers import  StaffSerializer, DutySerializer, AllocSerializer, AllocPostSerializer
from django.views.decorators.csrf import csrf_exempt
from .forms import UserForm, ProfileForm
from django.contrib import messages
from api.serializers import ToDoSerializer, UserSerializer
from api.models import ToDo
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request, f'Registration complete! You may log in!')
            return redirect('login')
    else:
        u_form = UserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'role': user.profile.role
    }


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        user_all = User.objects.all()
        serialiser = UserSerializer(user_all, many = True)
        return JsonResponse(serialiser.data, safe = False)


@csrf_exempt
@api_view(['GET', 'POST',])
@permission_classes([IsAuthenticated,])
def staff_list(request): 
    if request.method == 'GET':
        staff_all = Staff.objects.all()
        serialiser = StaffSerializer(staff_all, many = True)
        return JsonResponse(serialiser.data, safe = False)

    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serialiser = StaffSerializer(data=data)    
        
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status=400)    

@csrf_exempt
def duty_list(request):
    if request.method == 'GET':
        duty_all = Duty.objects.all()
        serialiser = DutySerializer(duty_all, many = True)
        return JsonResponse(serialiser.data, safe = False)

    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serialiser = DutySerializer(data=data)    
        
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status=400)   

@csrf_exempt
def alloc_list(request):
    if request.method == 'GET':
        alloc_all = Alloc.objects.all()
        serialiser = AllocSerializer(alloc_all, many = True)
        return JsonResponse(serialiser.data, safe = False)

    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serialiser = AllocPostSerializer(data=data)    
        
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status=400)

@csrf_exempt
def todo(request):
    if request.method == 'GET':
        toDo_all = ToDo.objects.all()
        serialiser = ToDoSerializer(toDo_all, many = True)
        return JsonResponse(serialiser.data, safe = False)

    elif request.method == 'POST':
        
        data = JSONParser().parse(request)
        serialiser = ToDoSerializer(data=data)    
        
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status=201)
        return JsonResponse(serialiser.errors, status=400)         
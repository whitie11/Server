from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import mimetypes
from DjangoProject.settings import BASE_DIR, MEDIA_ROOT

from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from libraryApp.serializers import FileSerializer
from libraryApp.models import File

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def index(request):
    return HttpResponse("Hello, world. You're at the library index.")    

@api_view(['POST']) 
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def download_file(request):
     data = JSONParser().parse(request)
     filename = data['fileStr']
     # fill these variables with real values
     # filename = "/PRH_Map_1000x750_2016_March_web.pdf"
     fl_path = MEDIA_ROOT + filename
     

     fl = open(fl_path, 'rb')
     mime_type, _ = mimetypes.guess_type(fl_path)
     response = HttpResponse(fl, content_type=mime_type)
     response['Content-Disposition'] = "attachment; filename=%s" % filename
     return response     

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
@csrf_exempt
def get_file_details(request):
    if request.method == 'GET':
        file_details = File.objects.all()
        serialiser = FileSerializer(file_details, many=True)
        return JsonResponse(serialiser.data, safe=False)
    return JsonResponse(serialiser.errors, status=400)     
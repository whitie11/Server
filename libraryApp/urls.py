from django.urls import path
from libraryApp.views import FileUploadView, download_file, get_file_details

urlpatterns = [
    path('upload/', FileUploadView.as_view()),
    path('download/', download_file),
    path('details/', get_file_details )    


]
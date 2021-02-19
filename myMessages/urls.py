from django.urls import path

from . import views
from myMessages.views import all_messages, all_messages_from_date, archive_message, filtered_messages_from_date, save_message


urlpatterns = [
    path('', views.index, name='index'),
    path('all_messages/', all_messages),
    path('save_message/', save_message),
    path('all_messages_from_date/', all_messages_from_date),
    path('filtered_messages_from_date/', filtered_messages_from_date),
    path('archive_message/', archive_message),
]
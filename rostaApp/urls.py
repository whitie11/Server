from django.urls import path

from . import views
from rostaApp.views import duties_from_date

urlpatterns = [
    path('duty_list/', duties_from_date),
]
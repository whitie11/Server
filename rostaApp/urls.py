from django.urls import path

from . import views
from rostaApp.views import duties_from_date, duty_staff_from_date, get_duties

urlpatterns = [
    path('duty_list/', duties_from_date),
    path('duties/', get_duties),
    path('duty_staff/', duty_staff_from_date),
]

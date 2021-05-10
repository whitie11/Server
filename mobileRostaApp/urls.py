from django.urls import path

from . import views
from mobileRostaApp.views import myduties_from_date

urlpatterns = [
    path('myduty_list/', myduties_from_date),

]
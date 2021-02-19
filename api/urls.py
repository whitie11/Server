from django.urls import path
from .views import staff_list, duty_list, alloc_list, register, todo
from api.views import user_list


urlpatterns = [
    path('staff/', staff_list),
    path('duty/', duty_list),
    path('alloc/', alloc_list),
    path('register/', register),
    path('todo/', todo),
    path('users/', user_list)
]
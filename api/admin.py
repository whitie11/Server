from django.contrib import admin
from .models import Staff, Duty, Alloc, Profile

# Register your models here.
admin.site.register(Staff)
admin.site.register(Duty)
admin.site.register(Alloc)
admin.site.register(Profile)


from django.db import models


class File(models.Model):
    description = models.CharField(max_length = 50)
    dateUploaded = models.DateTimeField(auto_now_add=True) 
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name

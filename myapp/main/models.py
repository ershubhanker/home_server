from django.db import models
import uuid, datetime
from django.contrib.auth.models import User
# Create your models here.



class Folder(models.Model):
    # folder_id = models.IntegerField(primary_key=True, default=1)
    parent = models.ForeignKey("self",on_delete=models.CASCADE, null=True)
    folder_name = models.CharField(max_length=50)
    folder_user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.folder_name}'

# class Inside_folder(models.Model):
#     folder = models.ForeignKey(Folder,on_delete=models.CASCADE)


# class FileUploadModel(models.Model):
#     from django.db import models

class FileUploadModel(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='file')
    filetitle = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return f'{self.file_name}'
    


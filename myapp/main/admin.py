from django.contrib import admin
from .models import FileUploadModel,Folder
# Register your models here.

# admin.site.register(FileUploadModel)
@admin.register(Folder)
class Administration(admin.ModelAdmin):
    list_display = ('folder_name','folder_user')

@admin.register(FileUploadModel)
class Administration(admin.ModelAdmin):
    list_display = ('id','file','file_name')

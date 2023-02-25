from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import FileUploadModel
from django.contrib.auth.models import User

class FileUploadForm(forms.Form):
    file = forms.FileField()

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','email', 'password1','password2']
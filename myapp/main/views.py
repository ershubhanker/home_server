from django.shortcuts import render,HttpResponse,redirect
from .models import FileUploadModel,Folder
from .forms import FileUploadForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout,login
# from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if username and email and password and confirm_password:
                if password == confirm_password:
                    user = User.objects.create_user(username,email,password)
                    user.username = username
                    user.save()

                    if user: 
                        messages.success(request,"You are inn...!")
                        return redirect('login')
                    else:
                        messages.error(request, "Fill those inputs")
                else:
                    messages.error(request, "password didn't match")
                    redirect('register')



        return render(request,'register.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
        return render(request, 'login_page.html')


def logout_page(request):
    logout(request)
    return redirect('index')


def folder(request,folderid):
    if request.user.is_authenticated:
        folder_user = Folder.objects.get(id=folderid)
        files = FileUploadModel.objects.filter(folder=folder_user)
        context = {'folderid':folderid,'files':files}
        if request.method == 'POST':
            file_user = request.FILES.get('file')
            file_title = request.POST.get('filetitle')
            fileadd = FileUploadModel.objects.create(filetitle=file_title,file=file_user,folder=folder_user)
        return render(request,'folder.html',context)
    else:
        return redirect('register')
    

def addFolder(request):
    if request.method == 'POST':
        folder_name = request.POST['folder_name']
        folder = Folder.objects.create(folder_name=folder_name,folder_user=request.user)

        if folder:
            return redirect('index')
        else:
            messages.error(request,'oops! folder not created')
            return redirect('index')
    # pass


def index(request):
    if request.user.is_authenticated:
        messages.success(request,"Welcome Home!")
        folder = Folder.objects.filter(folder_user=request.user)
        context = {'folder':folder}
        return render(request,'home.html',context)
    else:
        return redirect('register')
    








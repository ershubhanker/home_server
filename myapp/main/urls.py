from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_page, name='logout'),
    path('addFolder/',views.addFolder, name='addfolder'),
    path("folder/<int:folderid>/",views.folder, name='folder'),

]

from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/', views.login_page, name='login'),
    # path('register/', views.register, name='register'),
    path('logout/',views.logout_page, name='logout'),
    path('addFolder/',views.addFolder, name='addfolder'),
    path("folder/<int:folderid>/",views.folder, name='folder'),
    path('delete_file/<int:folderid>/<int:fileid>/', views.delete_file, name='delete_file'),
    path('delete_folder/<int:folderid>/', views.delete_folder, name='delete_folder'),

    path('reset-password/',auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset-password_sent/',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),

]

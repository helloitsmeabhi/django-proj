from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('edit/', views.edit, name="edit"),
    path('delete/', views.delete, name="delete"),
    path('addhandle/', views.addhandle, name="addhandle"),
    path('edithandle/', views.edithandle, name="edithandle"),
    path('deletehandle/', views.deletehandle, name="deletehandle"),
    path('thanks/', views.thanks, name="thanks"),  
    path('invaild/',views.invalid,name="invalid"),
]

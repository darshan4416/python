from django.contrib import admin
from django.urls import path, include
from .views import index, add, delete,update

urlpatterns = [
    path('', index,name="index"),
    path('add-emp/', add, name="add"),
    path('delete/<int:id>/', delete, name="delete"),
    path('update/<int:id>/', update)
]

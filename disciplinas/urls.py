from django.contrib import admin
from django.urls import path
from .views import disciplina, photos_class

urlpatterns = [
    path('<str:disciplina>/', disciplina, name="disciplina"),
    path('<str:disciplina>/photos_class/', photos_class, name="photos_class")
]
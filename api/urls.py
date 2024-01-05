from django.urls import path

from . import views

urlpatterns = [
    path('', views.ConvertText.as_view()),
    path('file', views.FileConverter.as_view()),
    path('migration', views.migration),
]

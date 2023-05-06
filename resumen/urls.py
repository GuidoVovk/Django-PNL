from . import views
from django.urls import path

urlpatterns = [
    path('', views.resumen, name='resumen'),
    
]
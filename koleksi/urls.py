from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sepatu/<int:sepatu_id>/', views.detail, name='detail'),
]
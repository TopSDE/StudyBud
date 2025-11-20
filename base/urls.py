from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'homeURL'),
    path('room_page/<str:pk>/', views.room, name = 'roomURL'),
    path('create-room/', views.CreateRoom, name = "create-roomURL")
]
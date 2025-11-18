from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'homeURL'),
    path('room_page/<str:pk>/', views.room, name = 'roomURL')
]
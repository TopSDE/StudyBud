from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('room_page/<str:pk>/', views.room, name = 'room')
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id' : 1, 'name' : "Lets learn Python!"},
#     {'id' : 2, 'name' : "Design With Me"},
#     {'id' : 3, 'name' : "Frontend Dev's"},
# ]
rooms = Room.objects.all()

def home(request):
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request, pk):
    room = Room.objects.get(id = pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i 
    
    context = {'room' : room}
    return render(request, 'base/room.html', context)

# Create your views here.

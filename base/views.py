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
    # return render(http://127.0.0.1:8000/, 'templates/base/home.html', rooms)
    # Together combined -> http://127.0.0.1:8000/templates/base/home.html

def room(request, pk):
    room = Room.objects.get(id = pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i 
    
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def CreateRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)
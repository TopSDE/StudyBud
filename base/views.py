from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id' : 1, 'name' : "Lets learn Python!"},
#     {'id' : 2, 'name' : "Design With Me"},
#     {'id' : 3, 'name' : "Frontend Dev's"},
# ]

def home(request):
    rooms = Room.objects.all()
    print("Rooms:", rooms)
    return render(request, 'base/home.html', {'rooms' : rooms})
    # return render(http://127.0.0.1:8000/, 'templates/base/home.html', rooms)
    # Together combined -> http://127.0.0.1:8000/templates/base/home.html
    # Djago first looks for Project(base)/Templates folder, and since 'APP_DIRS': True in
    # settings.py, it then look for base/templates/base folder

def room(request, pk):
    room = Room.objects.get(id = pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i 
    
    context = {'room' : room}
    return render(request, 'base/room.html', context)

def CreateRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeURL')

    context = {'form' : form}
    return render(request, 'base/room_form.html', context)
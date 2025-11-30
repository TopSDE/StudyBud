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
    # return render("", 'templates/base/home.html', rooms)
    # Together combined -> http://127.0.0.1:8000/templates/base/home.html
    # Djago first looks for Project(base)/Templates folder, and since 'APP_DIRS': True in
    # settings.py, it then look for base/templates/base folder

def room(request, pk):
    room = Room.objects.get(id=pk)
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
        # request.POST = new data submitted by user.
        # instance=room = old data from the database.

        # Django now knows:

        # ✔ merge the new POST data
        # ✔ with the old room instance
        # ✔ validate the form
        # ✔ save the updated record instead of creating new one

        if form.is_valid():
            form.save()
            return redirect('homeURL')

    context = {'form' : form}
    # print('This is ', request.path)
    return render(request, 'base/room_form.html', context)

def UpdateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    # instance - “Load this form with the existing values of this room object.”

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        # “Update this specific room using the new POST data.”
        if form.is_valid():
            form.save()
            return redirect('homeURL')

    context = {'form' : form}
    return render(request, 'base/room_form.html', context)

def DeleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    context = {'obj' : room}

    if request.method == "POST":
        room.delete()
        return redirect('homeURL')

    return render(request, 'base/delete.html', context)

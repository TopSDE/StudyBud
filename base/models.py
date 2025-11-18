from django.db import models
from django.contrib.auth.models import User

'''
Object → Python objects (ex: Room, Topic, Message)
Relational → Relational database (ex: MySQL, SQLite, PostgreSQL) --> Tables, columns, rows, IDs
Mapper → Mapping between the two --> Converts Python ↔ SQL

"from django.some_module import SomeClassOrFunction"
models → module/package (django.db.models).
Model → class inside that module.

makemigrations	-> Creates migration files (instructions).
migrate -> Executes instructions → creates/updates tables in DB.
'''
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) # Updates the timestamp every time the object is saved
    created = models.DateTimeField(auto_now_add=True) # Sets the timestamp once when the object is created

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
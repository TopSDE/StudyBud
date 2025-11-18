from django.contrib import admin

# snake_case → for functions & variables
# PascalCase / Upper Camel Case → for classes

from .models import Room, Topic, Message

# admin.site.register(Room) -> If we dont want customization, then we use this

@admin.register(Room) 
# -> “Register the Room model in the admin, 
# and the class below will control how it looks and behaves.”
class CustomRoomModel(admin.ModelAdmin):
    # list_display = ('id', 'name', 'topic', 'host', 'created', 'updated')
    readonly_fields = ('created', 'updated') 

admin.site.register(Topic)

@admin.register(Message)
class CustomMessageModel(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

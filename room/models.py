from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    host            = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic           = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name            = models.CharField(max_length= 200)
    description     = models.TextField(null=True, blank = True)     #* null is for database blank is for form
    #participants   =                                               #  active user in the room
    updated         = models.DateTimeField(auto_now=True)           #* time stamp every time there is change
    created         = models.DateTimeField(auto_now_add=True)        

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)     # SET_NULL - message will stay when room is deleted
    body = models.TextField()
    updated         = models.DateTimeField(auto_now=True)      
    created         = models.DateTimeField(auto_now_add=True)  

    def __STR__(self):
        return self.body[0:50]
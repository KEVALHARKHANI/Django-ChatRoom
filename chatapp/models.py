from django.db import models
from django.contrib.auth.models import User
from login.models import Student
# Create your models here.
class Chat_room(models.Model):
    name=models.CharField(max_length=300)
    message=models.CharField(max_length=800)
    image=models.ImageField(upload_to='room_pics')

class Activeuser(models.Model):
    name=models.CharField(max_length=300)
    connected=models.BooleanField(default=False)
    room=models.ForeignKey(Chat_room,models.CASCADE)
    user=models.ForeignKey(Student,on_delete=models.CASCADE)

class Chat_message(models.Model):
    message=models.CharField(max_length=900)
    datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Chat_room,models.CASCADE)
    student=models.ForeignKey(Student,models.CASCADE)






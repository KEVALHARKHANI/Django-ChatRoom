from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Activeuser,Chat_message,Chat_room
from login.models import Student
import time
# Create your views here.
class chat(ListView):
    def get(self,request,sem):
        active_user=Activeuser.objects.filter(connected=True,room=sem)
        chat_message = Chat_message.objects.filter(room=sem).order_by("datetime")
        room=Chat_room.objects.get(id=sem)
        return render(request, 'new_chat.html', {"room": room, "user": active_user, "chat": chat_message})

class Create_chat(ListView):
    def post(self,request):
        name=request.POST['name']
        msg=request.POST['msg']
        img=request.POST['img']
        room=Chat_room(name=name,message=msg,image=img)
        room.save()

class User(ListView):

    def get(self,request,id):
        photo = Student.objects.get(studentid=request.user)
        return render(request,'user.html',{'url':photo})

class Delete_photo(ListView):
    def get(self,request,id):
        return redirect("myprofile")


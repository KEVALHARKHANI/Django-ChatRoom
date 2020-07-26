from django.shortcuts import render,redirect
from login.models import Student
from django.contrib.auth.models import User
from chatapp.models import Chat_room,Activeuser
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        user=User.objects.get(username=request.user)
        user_data = Student.objects.get(studentid=user)
        room_data=Chat_room.objects.all()
        active_user={}
        for r in room_data:
            active=Activeuser.objects.filter(connected=True,room=r.id)
            active_user[r.id]=len(active)
        return render(request, 'home_main.html',{'user':user_data,'room':room_data,'active_user':active_user})
    else:
        return redirect('/login')



def chat_room(request,sem):
    print('sem: ',sem)
    return render(request,'chat_room.html')
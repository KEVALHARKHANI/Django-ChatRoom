from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')
def password(request):
    username=request.GET['username']
    userdata=User.objects.filter(username=username)
    print(userdata)
    for i in userdata:
        print(i.student.photo)
    if userdata:
        return render(request, 'login_password.html',{'userdata':userdata})
    else:
        messages.info(request,'invalid username')
        return redirect('/')
def check(request):
    username=request.POST['username']
    passwrd=request.POST['pass']
    print(username)
    user = auth.authenticate(username=username,password=passwrd)
    if user:
        auth.login(request,user)
        return redirect('home')
    else:
        messages.info(request,'invalid password')
        return HttpResponseRedirect('password?username='+username)


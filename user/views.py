from django.shortcuts import render,redirect
from login.models import Student
from django.views.generic import ListView
from .models import User_data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

# Create your views here.
class User(ListView):

    def get(self,request,id):
        photo = Student.objects.get(studentid=id)
        user=User.objects.get(id=id)
        return render(request,'user.html',{'url':photo})

class Upload(ListView):
    def post(self,request):
        files=request.FILES
        print(files)
        number=0
        file=None
        for x,y in files.items():
            if "file" in x:
                file=y
                number=x[4]
        print(number)
        number=int(number)
        if(file and number!=0):
            user=User_data.objects.filter(user=request.user)
            if(len(user)!=0):
                for i in user:
                    user=i
                if(user):
                    if (number == 1):
                        user.img1 = file
                    elif (number == 2):
                        user.img2 = file
                    elif (number == 3):
                        user.img3 = file
                    elif (number == 4):
                        user.img4 = file
                    elif (number == 5):
                        user.img5 = file
                    else:
                        user.img6 = file
                    user.save()
            else:
                if (number == 1):
                    user=User_data(user=request.user,img1=file)
                elif (number == 2):
                    user=User_data(user=request.user,img2=file)
                elif (number == 3):
                    user=User_data(user=request.user,img3=file)
                elif (number == 4):
                    user=User_data(user=request.user,img4=file)
                elif (number == 5):
                    user=User_data(user=request.user,img5=file)
                else:
                    user=User_data(user=request.user,img6=file)
                user.save()

        return redirect('myprofile')

    def update(self,file,number,user):
        number=int(number)

class My(ListView):
    def get(self,request):
        portfolio=User_data.objects.filter(user=request.user)
        if(len(portfolio)!=0):
            for i in portfolio:
                portfolio=i
        photo = Student.objects.get(studentid=request.user)
        return render(request,'user.html',{'url':photo,'photos':portfolio})
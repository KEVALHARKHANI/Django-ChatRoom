from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    studentid=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='pics')
    enroll_no=models.PositiveIntegerField()
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_data(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img1=models.ImageField(upload_to='portfolio',null=True)
    img2 = models.ImageField(upload_to='portfolio',null=True)
    img3 = models.ImageField(upload_to='portfolio',null=True)
    img4 = models.ImageField(upload_to='portfolio',null=True)
    img5 = models.ImageField(upload_to='portfolio',null=True)
    img6 = models.ImageField(upload_to='portfolio',null=True)



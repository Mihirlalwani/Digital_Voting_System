
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    # email=models.EmailField(max_length=200)
    voterId=models.CharField(max_length=200)
    pincode=models.IntegerField()
    image=models.ImageField(upload_to="images/")    
    if_voted=models.BooleanField(default=False)
    if_face_verified=models.BooleanField(default=False)



class VoteModel(models.Model):
    candidate_option=models.CharField(max_length=20)
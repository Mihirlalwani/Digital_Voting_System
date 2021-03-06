
from pickle import TRUE
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
    candidate_id=models.IntegerField(default=0,null=True ,blank=True)


# class VoteModel(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="vote")
   
    

class Candidte(models.Model):
    candidate_id=models.IntegerField()
    candidate_name=models.CharField(max_length=50)
    candidate_party=models.CharField(max_length=100)
    candidate_pincode=models.IntegerField()
    vote_count=models.IntegerField()

    def __str__(self):
        return self.candidate_name

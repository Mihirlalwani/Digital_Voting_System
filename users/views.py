from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegisterForm,VoteForm,UserProfileForm
from . models import UserModel,Candidte
from django.contrib.auth.decorators import login_required
import base64
from base64 import decodebytes
import users
import cv2
import os
import string    
import random
from PIL import Image
import numpy as np
from deepface import DeepFace
# Create your views here.


def home(request):
    return render(request,'users/home.html')


def register(request):
    # if request.method=='POST':
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST,request.FILES)
        profile_form=UserProfileForm(request.POST,request.FILES)
        username=request.POST['username']
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])            
            base64_img=(request.POST['base64_data'])
            # print(base64_img)
            image_name=save__image_file(base64_img)
            new_user.save()

            profile=profile_form.save(commit=False)
            profile.user=new_user        
            profile.image=image_name
            profile.save()

            messages.success(request, f'Hi {username}, Account created successfully!')
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        profile_form=UserProfileForm()
    return render(request,'users/register.html',{
        'user_form': user_form,
        'profile_form':profile_form
        })


def save__image_file(base64):
    b64_img=base64.replace("data:image/png;base64,","")
    byte_data = b64_img.encode('utf-8')
    ranndom_name = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 15)) + ".png")
    file_path=os.path.join(str(settings.MEDIA_ROOT) + "\images",ranndom_name)
    with open(file_path, "wb") as fh:
        fh.write(decodebytes(byte_data))
    return file_path




def cam_test(request):
    if request.method=='POST':
        # handle_uploaded_file()
        image=request.FILES['ajax_image']
        return  image
    else:
        return render(request,"users/cam_test.html")

def login(request):
    return render(request,'users/login.html')

@login_required()
def profile(request):
    if request.user.is_authenticated:
        user=request.user
        profile=request.user.profile
        print(profile.image.path)
    return render(request, 'users/profile.html',{
        'user':user,
        'profile':profile
    })

@login_required()
def vote(request):
    if request.method=="POST":
        form=VoteForm(request.POST)
        vote=request.POST['selected_candidate']
        print(vote)
        return HttpResponse("voted")
    else:        
        candidates=Candidte.objects.all()
        form=VoteForm()
        return render(request,"users/vote_form.html",{
            "form":form,
            "candidates":candidates,
            })



models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
@login_required
def verification(request):
    if request.method=="POST":
        # pass
        if request.user.is_authenticated:
            user_image_path=request.user.profile.image.path
        base64_image=request.POST['base64_data']
        temp_image=save_temp_image(base64_image)
        try:
            result = DeepFace.verify(img1_path = temp_image, img2_path = user_image_path, model_name = models[0])
        except:
            os.remove(temp_image)
            return HttpResponse("Not Verified")
        os.remove(temp_image)    
        print(result)
        return HttpResponse(result)
    else:
        return render(request,'users/verification.html')


backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe']

def cam_test(request):
    if request.method=='POST':
        base64_data=request.POST["base64_image"]
        temp_img=save_temp_image(base64_data)
        demography = DeepFace.analyze(img_path = temp_img, detector_backend = backends[4])
        # face = DeepFace.detectFace(img_path = temp_img, target_size = (224, 224), detector_backend = backends[4])
        print(demography)
        # print(face)
        os.remove(temp_img)

        return  HttpResponse("IMage Captured")
    else:
        return render(request,"users/cam_test.html")

def save_temp_image(base64):
    b64_img=base64.replace("data:image/png;base64,","")
    byte_data = b64_img.encode('utf-8')
    ranndom_name = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 15)) + ".png")
    file_path=os.path.join(str(settings.MEDIA_ROOT) + "\img_temp",ranndom_name)
    with open(file_path, "wb") as fh:
        fh.write(decodebytes(byte_data))
    return file_path
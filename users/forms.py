from dataclasses import field
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms    
from .models import UserModel

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserModel
        exclude=('if_voted','user','if_face_verified','image')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=('if_voted','if_face_verified','candidate_id')

class VoteForm(forms.Form):
    # choices = {'0':'Miti','1':'Mihir','2':'Ashwini'}
    cnadidate_option=forms.CharField(max_length=100);
    
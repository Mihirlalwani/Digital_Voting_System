from django.contrib import admin
from django.urls import path
from django.utils.regex_helper import normalize
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
path('',views.home, name='home'),
path('register/',views.register,name='register'),
path('profile/',views.profile,name='profile'),
path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
# path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
path('logout/',views.user_logout,name='logout'),
path('vote',views.vote,name="vote"),
path('verification',views.verification,name="verification"),

path('cam_test',views.cam_test,name="cam_test"),
path('election',views.election,name="election"),
path('contact',views.contact,name="contact")

]

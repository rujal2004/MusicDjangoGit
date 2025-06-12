from django.shortcuts import render
from musicbeats.models import Song,Watchlater
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def index(request):
    song = Song.objects.all()
    return render(request,'index.htm',{'song':song})

def songs(request):
    song = Song.objects.all()
    return render(request,'musicbeats/songs.html',{'song':song})

def songpost(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'musicbeats/songpost.html',{'song':song})




def user_login(request):
     if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect('/')
       
     return render(request,'musicbeats/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
       
        return redirect('/')
    return render(request,'musicbeats/signup.html')

from django.shortcuts import get_object_or_404, redirect, render
from .models import Song, Watchlater

def watchlater(request):
    if request.method == "POST":
        user = request.user
        tags = request.POST.get('tags')
        cond = True

        # Find the corresponding song using 'tags'
        song = get_object_or_404(Song, tags=tags)  # Ensure song exists
        
        # Save watchlater entry with song_id
        watchlater_entry = Watchlater(user=user, video_id=song.song_id)
        watchlater_entry.save()

        # Redirect using song_id instead of tags
        return redirect(f"/musicbeats/songs/{song.song_id}", {'cond': cond})  
    
    return render(request, 'musicbeats/watchlater.html')

from django.shortcuts import render
from musicbeats.models import Song
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def index(request):
    song = Song.objects.all()
    return render(request,'index.html',{'song':song})

def songs(request):
    song = Song.objects.all()
    return render(request,'musicbeats/songs.html',{'song':song})

def songpost(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'musicbeats/songpost.html',{'song':song})


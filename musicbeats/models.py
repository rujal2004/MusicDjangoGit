from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    song = models.FileField(upload_to='images/')
    #movie = models.CharField(max_length=100,default="")
    credit = models.CharField(max_length=100,default="")
    
    def __str__(self):
        return self.name

class Watchlater(models.Model):
      watch_id = models.AutoField(primary_key=True)
      user = models.ForeignKey(User,on_delete=models.CASCADE)#when user deleted his account then its history will be deleted
      video_id = models.CharField(max_length=100,default="")
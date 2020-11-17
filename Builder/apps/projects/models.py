from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, default=None)
    creator = models.ForeignKey(User, on_delete= models.CASCADE)
    co-owner = models.ManyToManyField(User, on_delete=models.CASCADE)
    world = models.ForeignKey(World)

class World(models.Model):
    name = models.CharField()
    characters
    

class Novel(models.Model):
    owner = models.ForeignKey(Container)
    chapter = models
        n-card = models.CharField()

class Chapter(models.Model)
    name = models.CharField()
    txt = models.TextField()


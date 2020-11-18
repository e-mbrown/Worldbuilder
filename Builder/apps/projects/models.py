from django.db import models, forms

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100, default=None)
    creator = models.ForeignKey('apps.auth.User', on_delete= models.CASCADE)
    co-owner = models.ManyToManyField('apps.auth.User', on_delete=models.CASCADE, blank=True, null=True)
    container = models.ForeignKey(World, blank=True, null=True)
    is_active = models.BooleanField(default=True)

class Container(models.Model):
    kind = models.CharField(max_length=255, default='Untitled')
    maps = model.ForeignKey(Map, blank=True, null=True)
    c-note = model.ForeignKey(Note, blank=True, null=True)
    catalog = model.ForeignKey(Catalog, blank=True, null=True)
    texts = model.ForeignKey(Text, blank=True, null=True)
    

class Text(form.Forms):
    body = models.FileField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)

class Catalog(models.Model):
    characters = models.ForeignKey(Character, blank=True, null=True)

class Character(form.Forms):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    hometown = models.CharField(max_length=255)
    other = models.FileField()




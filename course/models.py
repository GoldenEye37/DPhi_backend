from pyexpat import model
from django.db import models
from uuid import uuid4
from django.forms import CharField, SlugField
from django.contrib.auth.models import AbstractBaseUser as BaseUser
import course
from dphi_backend import settings

# Create your models here.



class Course(models.Model):
   
    title = models.CharField(max_length=255, unique=True, blank=True, null=True )
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    #educator = models.OneToOneField('Educator',on_delete=models.CASCADE)
    

    def __str__(self) -> str :

        return self.title

class Module(models.Model):
    module_title = models.CharField(max_length=255, unique=True, blank=True, null=True )
    description = models.TextField(blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    # content = models.TextField(blank=True, null=True, help_text="place module content") 


    def __str__(self) -> str :

        return self.title

class Content(models.Model):
    content_title = models.CharField(max_length=255, unique=True, blank=True, null=True )
    content = models.TextField(blank=True, null=True) 
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="contents")

    def __str__(self) -> str :

        return self.title

class Educator(AbstractBaseUser):
    experience = models.TextField(blank=True, null=True)



class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    user = models.ForeignKey(AbstractBaseUser, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

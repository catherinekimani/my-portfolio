from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField("pic")
    name = models.CharField(max_length=100)
    about = models.TextField()
    contact = models.EmailField(max_length=100)
    resume = CloudinaryField("resume")
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return f'{self.name}'
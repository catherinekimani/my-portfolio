from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField("pic")
    name = models.CharField(max_length=100)
    about = models.TextField()
    contact = models.EmailField(max_length=100)
    resume = CloudinaryField("resume",blank=True,null=True)
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
    
class About(models.Model):
    title = models.CharField(max_length=100)
    about_pic = CloudinaryField('about')
    about = models.TextField()
    contact = models.EmailField(max_length=100)
    
    def save_about(self):
        self.save()
        
    def delete_about(self):
        self.delete()
    
    def __str__(self):
        return f'{self.about}'
    
class Skills(models.Model):
    title = models.CharField(max_length=100)
    skills = models.TextField()
    skills_count = models.IntegerField()
    contact = models.EmailField(max_length=100)
    
    def save_skills(self):
        self.save()
        
    def delete_skills(self):
        self.delete()
    
    def __str__(self):
        return f'{self.skills}'
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    project_img = CloudinaryField('img')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return f'{self.project_img}'
    
class Contact(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    contact_img = CloudinaryField('img')
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.EmailField(max_length=100)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
    
    def __str__(self):
        return f'{self.title}'
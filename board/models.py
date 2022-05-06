from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from pytz import timezone
from ckeditor.fields import RichTextField

# The User Profile will allow Employers to view applicants
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(max_length=255)
    skills = models.TextField(max_length=255) #Comma seperated values for users skills
    avatar = models.ImageField(default='default.png', upload_to='uploads/avatars')
    resume = models.FileField(upload_to='uploads/resumes')

    def __str__(self):
        return self.user.username

# The employer model will post jobs on the board
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=30, default="Unknown Company")
    bio = models.TextField(max_length=255)
    avatar = models.ImageField(upload_to='uploads/avatars', default="default.png")
    banner = models.ImageField(upload_to='uploads/banners/', default="default.png")

    def __str__(self):
        return self.name + " | " + self.user.username
  



# Job posting model created by Employer
class Posting(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = RichTextField()
    tags = models.TextField(max_length=255) # Like the Profile.skills field, these will be comma seperated values 
    pub_date = models.DateTimeField('date published', default=datetime.now())

    class Meta:
        ordering = ['-pub_date'] 

    def __str__(self):
            return self.title + " | " + self.employer.name
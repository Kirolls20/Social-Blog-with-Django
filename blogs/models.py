from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Post Catogries
POST_CATOERY=(
    ('Programming Language','Programming Language'),
    ('Web Development', 'Web Development'),
    ('Algorithms And Data Strucure ','Algorithms And Data Strucure '),
    ('Front-End', 'Front-End'),
    ('Media','Media'),
    ('Marketing', 'Marketing'),
    ('Design','Design'),
    ('Research','Research'),
    ('Management','Management'),
    ('Other','Other')
)

class User(AbstractUser):
   #user = models.OneToOneField( settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   age = models.IntegerField(default=0)
   job_title = models.CharField(max_length=80)
   bio = models.TextField(default='Add Your Bio..')
   country=models.CharField(max_length=120)
   profile_pic = models.ImageField(null=True, blank=True, upload_to="images/")
   facebook_url = models.CharField(max_length=120, null=True, blank=True)
   insta_url = models.CharField(max_length=120, null=True, blank=True)
   twitter_url = models.CharField(max_length=120, null=True, blank=True)
   github_url = models.CharField(max_length=120, null=True, blank=True)


   def __str__(self):
      return self.username

class Post(models.Model):
  title = models.CharField(max_length=120)
  #body=models.TextField()
  body = RichTextField(blank=True, null=True)
  owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='post_owner')
  comments = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_commnet', through='Comment')
  likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes', blank=True)
  catogery = models.CharField(choices=POST_CATOERY, max_length=80)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def total_likes(self):
    return self.likes.count()

  def total_comments(self):
    return self.comments.count()

# This Code from Stackoverfow to solve capitalize categery problem
# https://stackoverflow.com/questions/11996963/how-to-automatically-capitalize-field-on-form-submission-in-django/12001244#12001244
  def save(self, *args, **kwargs):
      for field_name in ['catogery']:
          val = getattr(self, field_name, False)
          if val:
              setattr(self, field_name, val.capitalize())
      super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
  comment_body = models.TextField()
  owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.comment_body

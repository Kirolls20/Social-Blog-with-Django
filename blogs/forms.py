from django import forms 
from django.forms import ModelForm
from .models import Post,Comment,User

class CreatePostForm(ModelForm):
   class Meta:
      model=Post
      fields = ['title', 'body','catogery']

# Comment Form 
class CommentForm(ModelForm):
   class Meta:
      model=Comment
      fields= ['comment_body']
      
      
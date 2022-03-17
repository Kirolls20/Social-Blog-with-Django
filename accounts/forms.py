from django.contrib.auth.forms import SetPasswordForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField,UserCreationForm, UserChangeForm
from blogs.models import User

class UserLoginForm(AuthenticationForm):
   
   def __init__(self,*args,**kwargs):
      super(UserLoginForm,self).__init__(*args,**kwargs)
   
   username=UsernameField(widget=forms.TextInput())
   password=forms.CharField(widget=forms.PasswordInput())
# Create New User Form
class UserCreateForm(UserCreationForm):
   class Meta:
      model=User
      fields = ['first_name', 'last_name', 'username',
                'age', 'job_title', 'bio', 'country', 'profile_pic',
                'facebook_url', 'insta_url', 'twitter_url', 'github_url']

# Upate User Profile form 
class UserUpdateForm(UserChangeForm):
   class Meta:
      model=User
      fields = ['first_name', 'last_name', 'username',
                'age', 'job_title', 'bio', 'country', 'profile_pic',
                'facebook_url', 'insta_url', 'twitter_url', 'github_url']


# class MySetPasswordForm(SetPasswordForm):

#     def save(self, *args, commit=True, **kwargs):
#         user = super().save(*args, commit=False, **kwargs)
#         user.is_active = True
#         if commit:
#             user.save()
#         return user

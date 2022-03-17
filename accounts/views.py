from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy,reverse
from django.views import generic
from blogs.models import User,Post
from .forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import views as auth_views 
from django.contrib.auth.mixins import LoginRequiredMixin



class UserCreateView(generic.CreateView):
   template_name='registration/signup.html'
   model=User
   form_class=UserCreateForm

   def get_success_url(self):
      return reverse_lazy('login')

# User Profile View


class UserProfileView(LoginRequiredMixin,generic.DetailView):
   template_name = 'registration/user_profile.html'
   model=User
   
   # def  get_context_data(self, **kwargs):
   #     context = super().get_context_data(**kwargs)
   #     context["user_posts"] = Post.objects.filter(owner)
   #     return context
   
# Update User Profile View 
class UpdateUserProfileView(LoginRequiredMixin,generic.UpdateView):
   template_name = 'registration/update_user_profile.html'
   model=User
   form_class= UserUpdateForm

   def get_success_url(self):
      return reverse_lazy('post-list')

# Update User Password View 
class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
   template_name = 'registration/change-password.html'
   form_class = PasswordChangeForm
   def get_success_url(self):
      return reverse_lazy('login')


# # Reset password Confirm view 
# class ResetPassowrdView(auth_views.PasswordResetConfirmView):
#    template_name = 'registration/password_reset_form.html'
#    form_class = MySetPasswordForm

  


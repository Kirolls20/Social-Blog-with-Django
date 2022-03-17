from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserLoginForm

urlpatterns = [
    path('login/',LoginView.as_view(
       template_name='registration/login.html',
       authentication_form=UserLoginForm),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',views.UserCreateView.as_view(),name='signup'),
    path('user_profile/<int:pk>/', views.UserProfileView.as_view(),name='user-profile'),
    path('user/<int:pk>/update', views.UpdateUserProfileView.as_view(),name='update-profile'),
    path('user/password/', views.ChangePasswordView.as_view(),name='password-change'),
    # Process of reset the passwords
    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='registration/reset_password.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset_confirm'),
    
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_complete'),
    
]

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blogs.urls')),
    path('accounts/',include('accounts.urls')),
    
]
if settings.DEBUG:
    urlpatterns+static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)
    
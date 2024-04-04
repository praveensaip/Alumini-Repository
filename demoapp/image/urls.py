from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
  
urlpatterns = [
    path('image_upload/',views.avatarView, name = 'image_upload'),
    path('success/', views.uploadok, name = 'success'),
]
  
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
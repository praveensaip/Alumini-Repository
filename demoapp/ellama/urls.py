from django.urls import path
from .import views


urlpattern=[
    path('',views.chat_view,name='chat_view')
]
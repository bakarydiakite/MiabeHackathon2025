from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('discussion/', DiscussionViewSet.as_view(), name='discussion-list'),
    path('message/', MessageViewSet.as_view(), name='message-list'),
   
]
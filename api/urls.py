from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('endpoint/', endpointcreate.as_view(), name='post-list-creates'),
]

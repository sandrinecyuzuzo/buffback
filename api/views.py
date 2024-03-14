from rest_framework import generics
from .models import Post
from .serializers import *

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class endpointcreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = endpoints
    print("Seeo", serializer_class.data)

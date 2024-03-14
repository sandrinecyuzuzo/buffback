from rest_framework import serializers
from .models import Post
from .models import endpoint

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class endpoints(serializers.ModelSerializer):
    class Meta:
        model = endpoint
        fields = '__all__'

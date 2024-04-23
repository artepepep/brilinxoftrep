from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Modelserializer):
    
    class Meta:
        model = Post
        fields = '__all__'
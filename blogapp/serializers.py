from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  
    content = serializers.CharField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'tags', 'author', 'created_at', 'updated_at']




from rest_framework import serializers
from .models import Post, LANGUAGE_CHOICES, STYLE_CHOICES
from django.utils import timezone
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created_date', 'published_date')

"""class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = PrimaryKeyRelatedField(queryset=User.objects.all())
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    text = CharField(style={'base_template': 'textarea.html'})
    created_date = serializers.DateTimeField(required=False)
    published_date = serializers.DateTimeField(allow_null=True, required=False))

    def create(self, validated_data):
        
       # Create and return a new `Post` instance, given the validated data.
        
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
       # Update and return an existing `Post` instance, given the validated data.
        
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.code)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance"""
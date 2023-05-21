from rest_framework import serializers
from apps.comment.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'content', 'created_at', 'updated_at']
import django_filters

from .models import Comment

class CommentFilterSet(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ['user', 'product']  # Add relevant filter fields based on your requirements

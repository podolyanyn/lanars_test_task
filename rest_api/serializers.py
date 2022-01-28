from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Portfolio, Image, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username']


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['url', 'user', 'name', 'description']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['url', 'portfolio', 'name', 'description', 'picture']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'image', 'text']

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Portfolio, Image, Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PortfolioSerializer, ImageSerializer, CommentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PortfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ...
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ...
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ...
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticated]
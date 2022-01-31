from django.contrib.auth.models import User
from .models import Portfolio, Image, Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PortfolioSerializer, ImageSerializer, CommentSerializer
from rest_framework import filters
from .permissions import IsOwnerOrReadOnlyPortfolio, IsOwnerOrReadOnlyImage


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsOwnerOrReadOnlyPortfolio]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsOwnerOrReadOnlyImage]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

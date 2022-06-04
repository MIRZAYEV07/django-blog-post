from django.db.models import Q
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    ListAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from ..models import Post
from .serializers import (
    PostSerializer,
    PostDetailSerializer,

)
from .permissions import IsAuthorOrReadOnly, IsOwnerOrReadOnly


class PostAPIView(ListCreateAPIView):
    queryset = Post.objects.filter(Q(active=True) )
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(Q(active=True))
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    lookup_field = 'slug'


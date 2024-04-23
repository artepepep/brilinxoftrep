from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class GetCreatePosts(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetLastTenPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()[:10]


class GetFixAmountPostsAPI(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        quantity = self.kwargs.get('quantity', None)
        if quantity is not None:
            return Post.objects.all()[:quantity]
        return Post.objects.none()

from rest_framework import generics

from .models import Post, Section
from .serializers import PostSerializer, SectionSerializer
from users.permissions import CustomIsAdmin


class GetCreatePosts(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = (CustomIsAdmin, )

    queryset = Post.objects.all()


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


class GetCreateSection(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = (CustomIsAdmin, )

    queryset = Section.objects.all()
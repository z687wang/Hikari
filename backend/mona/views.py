from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from rest_flex_fields.views import FlexFieldsMixin, FlexFieldsModelViewSet
from rest_flex_fields import is_expanded
from .serializers import PostSerializer, ImageSerializer
from .models import Post, Image
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q
from rest_framework.response import Response


class PostViewSet(FlexFieldsMixin, ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permit_list_expands = ['category', 'comments', 'image']
    filterset_fields = ('category',)

    def get_queryset(self):
        queryset = Post.objects.all().filter(Q(public=True) | Q(author=self.request.user.id))

        if is_expanded(self.request, 'category'):
            queryset = queryset.prefetch_related('category')
        

        queryset = queryset.prefetch_related('image')

        if is_expanded(self.request, 'comments'):
            queryset = queryset.prefetch_related('comments')

        return queryset

class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all().filter(Q(public=True)| Q())
    permission_classes = [IsAuthenticated]
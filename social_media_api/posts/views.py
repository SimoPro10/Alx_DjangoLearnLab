from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from notifications.utils import create_notification
from rest_framework import status,generics
from django.contrib.contenttypes.models import ContentType


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@login_required
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({"error": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post owner
        notification = Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.id,
            target=post
        )

        return Response({"message": "Post liked successfully"}, status=status.HTTP_200_OK)
@login_required
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"error": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()  # Get users that the current user is following
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Get posts from followed users, ordered by creation date
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
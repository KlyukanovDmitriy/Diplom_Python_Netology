from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Comment, Like
from posts.permissons import IsOwnerOrReadOnly
from posts.serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Метод ограничения прав на действия с постом.
    def get_permissions(self):
        if self.action  in ["create", "destroy", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]

# Метод для автоматического назначения пользователя автором создаваемого поста.
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

# Метод для создания лайка
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if not Like.objects.filter(post=post, author=request.user).exists():
            Like.objects.create(post=post, author=request.user)
        return Response(status = status.HTTP_201_CREATED)

# Метод для удаления лайка
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id = post_id)
        like = get_object_or_404(Like, post = post, author = request.user)
        like.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Метод ограничения прав на действия с комментарием.
    def get_permissions(self):
        if self.action in ["create", "destroy", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [IsOwnerOrReadOnly()]

# Метод для автоматического назначения пользователя автором создаваемого комментария.
    def perform_create(self, serializer):
        serializer.save(post_id=self.kwargs['post_id'], author=self.request.user)





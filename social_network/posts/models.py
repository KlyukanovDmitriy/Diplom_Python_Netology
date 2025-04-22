from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Модель поста
class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to = 'images/', null=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.author}:{self.text}'


# Модель лайков к посту от пользователей
class Like(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'likes')

    def __str__(self):
        return f'{self.author}:{self.post}'


# Модель комментария
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.author}:{self.text}'

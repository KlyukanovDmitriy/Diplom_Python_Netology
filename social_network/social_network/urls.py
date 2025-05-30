"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, CommentViewSet, LikeView

Post_router = DefaultRouter()
Post_router.register('', PostViewSet)

CommentRouter = DefaultRouter()
CommentRouter.register('', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include(Post_router.urls)),
    path('api/posts/<int:post_id>/likes/', LikeView.as_view()),
    path('api/posts/<int:post_id>/comments/', include(CommentRouter.urls))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

from rest_framework.permissions import BasePermission

# Класс для создания разрешения "только на просмотр" всем пользователям, кроме автора
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.author
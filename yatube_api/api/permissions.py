from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверяет является ли юзер автором поста/коммента
       и какой метод запроса к эндпоинту."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

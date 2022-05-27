from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверяет является ли юзер автором поста/коммента
       и какой метод запроса к эндпоинту."""
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)

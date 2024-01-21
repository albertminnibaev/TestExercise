from rest_framework.permissions import BasePermission


class IsActiv(BasePermission):
    message = 'У вас нет права доступа, обратитесь к администратору'

    def has_permission(self, request, view):
        return request.user.is_active

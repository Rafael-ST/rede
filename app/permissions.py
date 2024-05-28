from rest_framework import permissions

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsLider(permissions.BasePermission):
    """
    Permissão para permitir acesso apenas aos usuários do grupo 'Lider'.
    """

    def has_permission(self, request, view):
        # Verifique se o usuário está autenticado
        if not request.user or not request.user.is_authenticated:
            return False

        # Verifique se o usuário pertence ao grupo 'Lider'
        return request.user.groups.filter(name='Lider').exists()
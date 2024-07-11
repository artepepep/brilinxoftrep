from rest_framework import permissions


class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(not request.user.is_anonymous and request.user.admin_role == 'Superadmin')


class CustomIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(not request.user.is_anonymous and request.user.admin_role == 'Admin')
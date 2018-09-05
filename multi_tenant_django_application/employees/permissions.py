from rest_framework.permissions import BasePermission, SAFE_METHODS


class CompanyAdminOrSelf(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user == obj.company.admin or request.method in SAFE_METHODS:
            return True

        return obj.employee == request.user

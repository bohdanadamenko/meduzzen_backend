from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance check for 'owner' attribute and additional check to ensure 'owner' is not None
        has_owner = hasattr(obj, 'owner') and obj.owner is not None

        # Write permissions are only allowed to the owner of the object or to admins.
        return (
            obj == request.user or
            (has_owner and obj.owner == request.user) or
            request.user.is_staff
        )

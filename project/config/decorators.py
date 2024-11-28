"""
Module: decorators

This module contains custom decorators for the project.
"""

from functools import wraps

from django.core.exceptions import PermissionDenied


def admin_or_superuser_required(view_func):
    """Decorator to check if the user is an admin or a superuser."""

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        """Check if the user is an admin or a superuser."""
        if not request.user.is_authenticated and not request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)

    return _wrapped_view

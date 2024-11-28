"""
Module: user forms

This module provides forms for the user app.
"""

from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating a new user. Inherits from UserCreationForm.

    Inherites from UserCreationForm, which is a built-in form for
    creating a new user.
    """

    class Meta:
        """Metadata for the CustomUserCreationForm."""

        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating an existing user. Inherits from UserChangeForm.

    Inherites from UserChangeForm, which is a built-in form for updating an
    existing user.
    """

    class Meta:
        """Metadata for the CustomUserChangeForm."""

        model = CustomUser
        fields = ("email",)

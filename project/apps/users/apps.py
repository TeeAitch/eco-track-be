"""
Module: user apps

This module defines the configuration class for the user app.
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    """Configuration class for the user app."""

    name = "users"
    verbose_name = _("Users")

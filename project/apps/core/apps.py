"""
Module: apps

Provides Django app configuration for the 'core' app.
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    """App configuration for the 'core' app."""

    name = "core"
    verbose_name = _("Core")

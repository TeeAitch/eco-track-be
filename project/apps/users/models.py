"""
Module: user models

This module defines custom user-related models and their managers for a Django
application. It includes a custom user model that uses email for authentication
instead of a username, and a user profile model for additional user
information.
"""

from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    Model managers encapsulate the logic for interacting with a Django model's
    database table. The `CustomUserManager` is responsible for creating and
    managing instances of the `CustomUser` model.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields to set for the user.

        Returns:
            CustomUser: The newly created user.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password for the user.
            **extra_fields: Additional fields to set for the user.

        Returns:
            CustomUser: The newly created superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """Custom user model representing a user in the system."""

    id = models.UUIDField(
        max_length=36,
        primary_key=True,
        default=uuid4,
        editable=False,
        help_text=_("The unique identifier for the object."),
    )
    email = models.EmailField(
        verbose_name=_("Email address"),
        max_length=255,
        unique=True,
        help_text=_("The oganisation email address for the user."),
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Firstname"),
        help_text=_("The first name of the user."),
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Lastname"),
        help_text=_("The last name of the user."),
    )
    username = None
    is_staff = models.BooleanField(
        default=True,
        help_text=_("Indicates whether the user is a staff member."),
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        """
        Overwrite the save method to set the first and last name
        based on the email, if they are not set.
        """
        if not self.first_name:
            self.first_name = self.email.split("@")[0][:1].upper()
        if not self.last_name:
            self.last_name = self.email.split("@")[0][1:2].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        """Str representation of the object."""
        return self.get_full_name()

    def get_groups(self):
        """Returns a list of group names that the user belongs to."""
        return [
            # pylint: disable=no-member
            group.name
            for group in self.groups.all()
        ]

    get_groups.short_description = _("Groups")

    def get_is_admin(self):
        """Returns whether the user is an admin."""
        return self.is_superuser

    get_is_admin.boolean = True
    get_is_admin.short_description = _("Admin")

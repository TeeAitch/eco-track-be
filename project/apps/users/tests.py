"""
Module: user tests

This module contains test cases for the CustomUser and Profile models. The test
cases cover various functionalities including user creation, profile creation,
custom save methods, and specific model methods.
"""

from django.test import TestCase

from .models import CustomUser


class CustomUserModelTests(TestCase):
    """
    Test suite for the CustomUser model.
    """

    def setUp(self):
        """
        Set up test environment by initializing common test data.
        """
        self.email = "test@example.com"
        self.password = "testpass123"

    def test_create_user(self):
        """
        Test creating a regular user.
        """
        user = CustomUser.objects.create_user(
            email=self.email,
            password=self.password,
            is_staff=False,
            is_superuser=False,
        )
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """
        Test creating a superuser.
        """
        superuser = CustomUser.objects.create_superuser(
            email=self.email,
            password=self.password,
            is_staff=True,
            is_superuser=True,
        )
        self.assertEqual(superuser.email, self.email)
        self.assertTrue(superuser.check_password(self.password))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_custom_user_save_method(self):
        """
        Test the custom save method in the CustomUser model.
        """
        user = CustomUser.objects.create_user(
            email=self.email, password=self.password
        )
        user.first_name = ""
        user.last_name = ""
        user.save()
        self.assertEqual(user.first_name, "T")
        self.assertEqual(user.last_name, "E")

    def test_get_full_name(self):
        """
        Test the get_full_name method.
        """
        user = CustomUser.objects.create_user(
            email=self.email, password=self.password
        )
        user.first_name = "Test"
        user.last_name = "User"
        self.assertEqual(user.get_full_name(), "Test User")

    def test_get_groups(self):
        """
        Test the get_groups method.
        """
        user = CustomUser.objects.create_user(
            email=self.email, password=self.password
        )
        self.assertEqual(user.get_groups(), [])

    def test_get_is_admin(self):
        """
        Test the get_is_admin method for superusers.
        """
        user = CustomUser.objects.create_superuser(
            email=self.email, password=self.password
        )
        self.assertTrue(user.get_is_admin())

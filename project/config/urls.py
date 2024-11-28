"""
Module: config.urls

URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .decorators import admin_or_superuser_required as perm

# api urls
api_patterns = [
    # path("", include("users.urls")),
]

docs_patterns = [
    path(
        "redoc/",
        perm(SpectacularRedocView.as_view(url_name="schema")),
        name="redoc",
    ),
    path(
        "swagger-ui/",
        perm(SpectacularSwaggerView.as_view(url_name="schema")),
        name="swagger-ui",
    ),
    path(
        "schema/",
        perm(SpectacularAPIView.as_view()),
        name="schema",
    ),
]

# urls with translations
urlpatterns = i18n_patterns(
    path("i18n/", include("django_translation_flags.urls")),
    path("documentation/", include(docs_patterns)),
    path("api/v1/", include(api_patterns)),
    path("", admin.site.urls),
)

# if in debug mode, add static and media urls
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )

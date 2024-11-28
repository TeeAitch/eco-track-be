"""
Module: i18n_switcher

Provides Django template filters for switching language codes in URL paths.
"""

from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()


def switch_lang_code(path, language):
    """
    Switches the language code in a given URL path.

    Args:
        path (str): The URL path to modify.
        language (str): The new language code.

    Returns:
        str: The modified URL path with the new language code.

    Raises:
        Exception: If the URL path is empty, doesn't start with "/",
                   or the language code is not supported.
    """
    # Get the supported language codes
    lang_codes = [c for (c, name) in settings.LANGUAGES]

    # Validate the inputs
    if not path:
        raise ValueError("URL path for language switch is empty")
    if not path.startswith("/"):
        raise ValueError(
            'URL path for language switch does not start with "/"'
        )
    if language not in lang_codes:
        raise ValueError(f"{language} is not a supported language code")

    # Split the parts of the path
    parts = path.split("/")

    # Add or substitute the new language prefix
    if parts[1] in lang_codes:
        parts[1] = language
    else:
        parts[0] = "/" + language

    # Return the full new path
    return "/".join(parts)


@register.filter
@stringfilter
def switch_i18n_prefix(path, language):
    """
    Django template filter: Switches the language code in a given URL path.

    Usage:
        {{ some_path|switch_i18n_prefix:"en" }}

    Args:
        path (str): The URL path to modify.
        language (str): The new language code.

    Returns:
        str: The modified URL path with the new language code.
    """
    return switch_lang_code(path, language)


@register.filter
def switch_i18n(request, language):
    """
    Django template filter: Switches the language code in the URL path
    of a request.

    Usage:
        {{ request|switch_i18n:"en" }}

    Args:
        request (HttpRequest): The request object.
        language (str): The new language code.

    Returns:
        str: The modified URL path with the new language code.
    """
    return switch_lang_code(request.get_full_path(), language)

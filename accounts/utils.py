import re

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.sites.shortcuts import get_current_site
from django.core import exceptions
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls.base import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode

import six

from .tokens import account_activation_token

CHALLENGE_DEFAULT_BYTE_LEN = 32
UKEY_DEFAULT_BYTE_LEN = 20
USERNAME_MAX_LENGTH = 32
DISPLAY_NAME_MAX_LENGTH = 65


def check_lecturer_username(username):
    if not username.lower().endswith("@futa.edu.ng"):
        return False
    return True


def validate_username(username):
    if get_user_model().objects.filter(username=username).exists():
        return {
            "success": False,
            "reason": "User with that matriculation number already exists",
        }
    if not isinstance(username, six.string_types):

        return {
            "success": False,
            "reason": "Matriculation number should be alphanumeric",
        }

    if len(username) > USERNAME_MAX_LENGTH:
        return {
            "success": False,
            "reason": "Matriculation number too long",
        }

    if not username.isalnum():

        return {
            "success": False,
            "reason": "Matriculation number should be alphanumeric",
        }

    if not username.lower().startswith("cpe"):
        return {
            "success": False,
            "reason": "Matriculation number is not valid",
        }

    return {
        "success": True,
    }


def validate_email(email):
    if get_user_model().objects.filter(email=email).exists():
        return {"success": False, "reason": "Email Address already exists"}
    if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        return {"success": False, "reason": "Invalid Email Address"}
    if email is None:
        return {"success": False, "reason": "Email is required."}
    return {"success": True}


def is_valid_email(email):
    if get_user_model().objects.filter(email=email).exists():
        return False
    if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        return False
    if email is None:
        return False
    return True


def is_valid_username(username):
    if get_user_model().objects.filter(username=username).exists():
        return False
    if not username.lower().startswith("cpe"):
        return False
    return True


def is_password_validated(password, user):
    try:
        validate_password(password, user=user)
    except exceptions.ValidationError:
        return False
    return True


def registeration_helper(request, post_data, is_student=True):
    res = {
        "success": False,
        "msg": "Password is too weak! Ensure you adhere to all the specidied measures.",
    }
    if is_valid_email(post_data.get("email")):
        user = get_user_model().objects.create(email=post_data.get("email"))
    else:
        return JsonResponse(
            {
                "success": False,
                "msg": "Email address is not valid or already taken",
            }
        )
    if is_valid_username(post_data.get("username").replace("/", "")):
        return JsonResponse(
            {
                "success": False,
                "msg": "Username is not valid or already taken",
            }
        )
    user.username = post_data.get("username").replace("/", "")
    user.first_name = post_data.get("first_name")
    user.last_name = post_data.get("last_name")
    user.level = post_data.get("level")
    user.gender = post_data.get("gender")
    password = post_data.get("password1")
    if is_password_validated(password, user):
        user.set_password(password)
        user.is_active = False
        if is_student:
            user.is_student = True
        else:
            user.is_lecturer = True
        user.save()
        current_site = get_current_site(request)
        subject = "Please Activate Your Student Account"
        ctx = {
            "user": user,
            "domain": current_site,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
        }
        if settings.DEBUG:
            message = render_to_string("accounts/activation_request.txt", ctx)
        else:
            message = render_to_string("accounts/activation_request.html", ctx)
        plain_message = strip_tags(message)
        user.email_user(subject, plain_message, html_message=message)
        username = post_data.get("username").replace("/", "")
        raw_password = password
        user = authenticate(username=username, password=raw_password)
        return JsonResponse(
            {
                "success": True,
                "msg": "Your account has been created! You need to verify your email address to be able to log in.",
                "next": reverse("accounts:activation_sent"),
            }
        )
    else:
        get_user_model().objects.get(email=post_data.get("email")).delete()
    return JsonResponse(res)

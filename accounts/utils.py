import re
import secrets
import string

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

import pytz
import six

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


def validate_email_lecturer(email):
    if get_user_model().objects.filter(email=email).exists():
        return {"success": False, "reason": "Email Address already exists"}
    if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        return {"success": False, "reason": "Invalid Email Address"}
    if email is None:
        return {"success": False, "reason": "Email is required."}
    if not email.lower().endswith("@futa.edu.ng"):
        return {"success": False, "reason": "Email is not recognized."}
    return {"success": True}


def is_valid_email_lecturer(email):
    if get_user_model().objects.filter(email=email).exists():
        return False
    if not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        return False
    if email is None:
        return False
    if not email.lower().endswith("@futa.edu.ng"):
        return False
    return True


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


def random_string_generator(size=10, chars=string.ascii_lowercase):
    return "".join(secrets.choice(chars) for _ in range(size))

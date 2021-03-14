import jwt
import time
import copy
import json

# One hour in seconds times 1000 to convert from milliseconds to seconds.
_token_valid_length = 3600*1000

# This should be in an environment variable or retrieved from a secrets vault.
_security_secret = "secret"


# This is a hack for demo purposes only. Systems go to a password/directory to valid password.
_user_info = {
    "admin@contoso.org": {
        "firstName": "Admin",
        "lastName": "Dude",
        "password": "admin",
        "email": "admin@contoso.org"
    },
    "fan@contoso.org": {
        "firstName": "Fan",
        "lastName": "Dude",
        "password": "admin",
        "email": "fan@contoso.org"
    }
}


def _get_user_info(email):
    result = _user_info.get(email, None)
    return result


def _validate_password(email, password):

    u_info = _get_user_info(email)

    # We would not store password in the clear. We would store a hashed version
    # and then hash the in coming password to check for a match.
    if u_info is not None and u_info["password"] == password:
        result = True
    else:
        result = False

    return result


def _generate_user_token(u_info):

    t_info = copy.deepcopy(u_info)
    del t_info["password"]
    token_signed = jwt.encode(t_info, _security_secret)
    t_info["signature"] = token_signed

    return t_info


def _validate_user_token(t_info):

    try:
        tmp = copy.deepcopy(t_info)
        sig = t_info["signature"]
        del tmp["signature"]

        cmp = jwt.encode(tmp, _security_secret)

        if cmp == sig:
            result = True
        else:
            result = False
    except Exception as e:
        print("_validate_user_token, e = ", e)
        result = False

    return result







from functools import wraps
from flask import request, abort


def user_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not request.headers.get("X-User-Id"):
            abort(401)
        return fn(*args, **kwargs)
    return wrapper


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if request.headers.get("X-Admin-Token") != "expected-admin-token":
            abort(403)
        return fn(*args, **kwargs)
    return wrapper

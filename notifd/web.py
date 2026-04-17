from functools import wraps
from flask import Flask, jsonify

app = Flask(__name__)


def json_route(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            data = fn(*args, **kwargs)
            return jsonify({"ok": True, "data": data})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500
    return wrapper

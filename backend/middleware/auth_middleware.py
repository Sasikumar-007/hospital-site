from functools import wraps
from flask import request, jsonify, g
import jwt
from config import Config


def jwt_required(allowed_roles=None):
    allowed_roles = allowed_roles or []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization", "")
            if not auth_header.startswith("Bearer "):
                return jsonify({"error": "Missing bearer token"}), 401

            token = auth_header.split(" ", maxsplit=1)[1]
            try:
                payload = jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])
                role = payload.get("role")
                if allowed_roles and role not in allowed_roles:
                    return jsonify({"error": "Forbidden"}), 403
                g.user = payload
            except jwt.PyJWTError:
                return jsonify({"error": "Invalid token"}), 401

            return func(*args, **kwargs)

        return wrapper

    return decorator

from flask import request, g, jsonify


def fake_auth():
    user_id = request.headers.get("X-User-Id")
    role = request.headers.get("X-User-Role")

    if not user_id or not role:
        return jsonify({"error": "Authentication required"}), 401

    g.user = {
        "id": int(user_id),
        "role": role
    }

from flask import Blueprint, jsonify

tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.route("/health", methods=["GET"])
def tickets_health():
    return jsonify({"tickets": "ok"})

from flask import Blueprint, request, jsonify
from .services import create_ticket


tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.route("/", methods=["POST"])
def create():
    # fake user for now
    user = {"id": 1, "role": "customer"}

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "JSON body required"}), 400

    question = data.get("question")

    if not question or not isinstance(question, str):
        return jsonify({"error": "Question is required"}), 400

    if len(question) > 500:
        return jsonify({"error": "Question too long"}), 400

    ticket = create_ticket(data, user)

    return jsonify(ticket), 201

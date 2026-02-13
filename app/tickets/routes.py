from flask import Blueprint, request, g, jsonify
from .services import create_ticket
from .store import tickets


tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.route("/", methods=["POST"])
def create():
    # AUTHORIZATION (not authentication)
    if g.user["role"] != "customer":
        return jsonify({"error": "Forbidden"}), 403

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "JSON body required"}), 400

    question = data.get("question")

    if not question or not isinstance(question, str):
        return jsonify({"error": "Question is required"}), 400

    if len(question) > 500:
        return jsonify({"error": "Question too long"}), 400

    ticket = create_ticket(data, g.user)

    return jsonify(ticket), 201


@tickets_bp.route("/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ticket = tickets.get(ticket_id)

    if not ticket:
        return jsonify({"error": "Not found"}), 404

    user = g.user

    if user["role"] == "customer" and ticket["owner_id"] != user["id"]:
        return jsonify({"error": "Forbidden"}), 403

    return jsonify(ticket)

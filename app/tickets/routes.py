from flask import Blueprint, request, jsonify
from .services import create_ticket


tickets_bp = Blueprint("tickets", __name__)


@tickets_bp.route("/", methods=["POST"])
def create():
    # fake user for now
    user = {"id": 1, "role": "customer"}

    data = request.get_json()
    ticket = create_ticket(data, user)

    return jsonify(ticket), 201

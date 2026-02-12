from flask import Flask
from app.auth import fake_auth


def create_app():
    """Application factory for SupportHub"""
    app = Flask(__name__)

    app.before_request(fake_auth)

    # register blueprints
    from app.tickets.routes import tickets_bp
    app.register_blueprint(tickets_bp, url_prefix="/tickets")

    return app

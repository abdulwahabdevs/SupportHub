from flask import Flask


def create_app():
    """Application factory for SupportHub"""
    app = Flask(__name__)

    # register blueprints
    from app.tickets.routes import tickets_bp
    app.register_blueprint(tickets_bp, url_prefix="/tickets")

    return app

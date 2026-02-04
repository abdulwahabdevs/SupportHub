from flask import Flask


def create_app():
    """Application factory for SupportHub"""
    app = Flask(__name__)

    # Temporary minimal route
    @app.route("/health")
    def health():
        return {"status": "OK"}

    return app

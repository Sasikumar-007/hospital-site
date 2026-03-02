from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes.api import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, origins=[Config.FRONTEND_ORIGIN])

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"})

    app.register_blueprint(api, url_prefix="/api")
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

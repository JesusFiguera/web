import os
from flask import Flask
import secrets

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=secrets.token_hex(16),
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )
    import db
    db.init_app(app)

    import auth
    import user
    import trivia
    app.register_blueprint(trivia.bp)
    app.register_blueprint(user.bp)
    app.register_blueprint(auth.bp)

    return app


app = create_app()
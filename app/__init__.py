from flask import Flask
from app.routes import routes
from app.utils.general import check_pwned_password

def create_service():
    app = Flask(__name__)
    routes(app, check_pwned_password)
    return app

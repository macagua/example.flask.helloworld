from flask import Flask

def hello_world():
    return "<p>Hello, World!</p>\n"

def create_app():
    app = Flask(__name__)
    app.get("/")(hello_world)
    return app

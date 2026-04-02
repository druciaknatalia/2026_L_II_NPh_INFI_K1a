from flask import jsonify

from hello_world import app


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/hello")
def hello():
    return "Hello, NataliaD!"


@app.route("/output")
def output():
    return "Hello from output!"


@app.route("/output-json")
def output_json():
    return jsonify({"message": "Hello, World!"})

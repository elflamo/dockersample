from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "URL home"})


@app.route("/name")
def name():
    return jsonify({"message": "URL name"})


if __name__ == "__main__":
    app.run(debug=True)

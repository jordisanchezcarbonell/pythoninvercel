from flask import Flask, Response
app = Flask(__name__)


@app.route("/")
def home():
    return "API is working fine"


if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0", port=5000)

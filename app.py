from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("Hello, flask app" + os.environ["TELEGRAM_KEY"])
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/login")
def login():
    return "login!!"


if __name__ == "__main__":
    app.run(debug=True)

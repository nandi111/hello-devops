from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps! This is my simple HTTP app."

if __name__ == "__main__":
    # 0.0.0.0 + 8080, hogy a feladat követelményének megfeleljünk
    app.run(host="0.0.0.0", port=8080)

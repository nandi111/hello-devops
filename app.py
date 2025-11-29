from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOpsz! Ez egy szimpla HTTP appppp, most már egy feature branch változtatással."

@app.route("/info")
def info():
    return "Ez egy /info végpont. Feature branch részeként lett hozzáadva a DevOps részeként."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Job Hunter version 2 - CI/CD Demo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

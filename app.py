from flask import Flask, request, make_response, render_template

app = Flask(__name__)

click = 0
@app.route("/")
def main():
    return render_template("index.html")

app.run(debug=True)
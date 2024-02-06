from flask import Flask

app = Flask("mickael-levy")

@app.route("/")
def hello():
    return "<p>Bonjour Mickael</p>"


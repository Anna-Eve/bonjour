
from flask import Flask

app = Flask(__name__)

@app.route("/b")
def root():
    return "Hello world"


app.run()
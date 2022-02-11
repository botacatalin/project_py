from unicodedata import name
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
@app.route("/")
def home(name=None):
    return render_template("home.html",name=escape(name))

if __name__ == '__main__':
    app.run(debug=True)
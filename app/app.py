from unicodedata import name
from flask import Flask
from flask import render_template
from markupsafe import escape
import logging
from flask import request

app = Flask(__name__)
# logging.basicConfig(filename='logs/log.log', encoding='utf-8', level=logging.DEBUG)

@app.route("/<name>")
@app.route("/")
def home(name=None):
    # app.logger.info('app started ...')
    return render_template("home.html",name=escape(name))

if __name__ == '__main__':
    app.run(debug=True)
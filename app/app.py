from unicodedata import name
from flask import Flask
from flask import render_template
from markupsafe import escape
import logging

app = Flask(__name__)
# logging.basicConfig(filename='logs/log.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/<name>")
@app.route("/")
def home(name=None):
    # app.logger.info('app started ...')
    return render_template("home.html",name=escape(name))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Blueprint
from flask import render_template
from markupsafe import escape

routes = Blueprint('routes',__name__)

@routes.route("/<name>")
@routes.route("/")
def home(name=None):
    return render_template("home.html",name=escape(name))

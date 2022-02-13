from flask import Blueprint, render_template, flash
from markupsafe import escape

routes = Blueprint('routes',__name__)

@routes.route("/<name>")
@routes.route("/")
def home(name=None):
    flash(escape(name),category='error')
    return render_template("home.html",name=escape(name))

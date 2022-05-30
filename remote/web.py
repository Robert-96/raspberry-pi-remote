from flask import Blueprint, render_template

from .actions import ACTIONS_CONTROLLER

bp = Blueprint("web", __name__, url_prefix="/")


@bp.route("/")
def index():
    return render_template("web/index.html", modes=ACTIONS_CONTROLLER.get_modes())

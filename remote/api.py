import json

from flask import Blueprint, abort, request, jsonify
from werkzeug.exceptions import HTTPException

from .actions import ACTIONS_CONTROLLER


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.errorhandler(HTTPException)
def handle_exception(error):
    """Return JSON instead of HTML for HTTP errors."""

    response = error.get_response()
    response.data = jsonify({
        "error": {
            "code": error.code,
            "name": error.name,
            "description": error.description,
        }
    })

    response.content_type = "application/json"
    return response


@bp.get("/coffee")
def coffee():
    abort(418)


@bp.get("/tea")
def tea():
    return jsonify({"tea": {"name": "Black Tea"}})


@bp.get("/modes")
def get_modes():
    return jsonify({"modes": ACTIONS_CONTROLLER.get_modes()})


@bp.get("/actions")
def get_actions():
    return jsonify({"actions": ACTIONS_CONTROLLER.get_actions()})


@bp.get("/actions/<mode>")
def get_actions_for_mode(mode):
    return jsonify({"actions": ACTIONS_CONTROLLER.get_actions(mode=mode)})


@bp.post("/actions")
def post_action():
    payload = request.get_json()
    action = payload["action"]

    try:
        response = ACTIONS_CONTROLLER.call_action(action)
    except KeyError:
        abort(404, description="Action named '{}' not found".format(action["name"]))

    return jsonify({"action": response}), 201

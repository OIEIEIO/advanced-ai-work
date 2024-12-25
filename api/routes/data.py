from flask import Blueprint

data_blueprint = Blueprint("data", __name__)


@data_blueprint.route("/info", methods=["GET"])
def get_data_info():
    return {"data": "Sample Data"}

import json
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

edit = Blueprint('edit', __name__, template_folder=".")


@edit.route('/edit/<uid>', methods=['GET', 'POST'])
def __edit(uid):
    if request.method == "GET":
        path = request.args.get("path")
        assert path
        _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": "edit", "data": {"path": path}})
        return render_template('edit.html', code=_data["raw"]["data"])
    else:
        path = request.args.get("path")
        data = json.loads(request.data)["data"]
        _data = current_app.cache[uid][0].send_term_command(
            {"v_uid": "0222", "type": "edit", "data": {"path": path, "data": data}})
        return jsonify(_data)

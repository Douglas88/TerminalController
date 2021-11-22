import base64
import json
from flask import Blueprint, request, render_template, jsonify
from config import SPEED, cache

file = Blueprint('file', __name__, template_folder=".")


@file.route('/file/<uid>', methods=['GET', 'POST'])
def __file(uid):
    if request.method == "GET":
        return render_template('file.html')
    elif request.form.get("dir"):
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "dir", "data": request.form.get("dir")})
        return jsonify({"code": 0, "data": _data["raw"]})
    elif request.form.get("action") == "upload":
        _file = request.files["file"]
        _path = request.form.get("src_path")
        _file_data = base64.b64encode(_file.read()).decode()
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "upload", "data": {"path": _path, "filename": _file.filename, "data": _file_data}})
        return jsonify(_data)
    else:
        data = json.loads(request.data)
        if data["action"] == "download":
            _data = cache[uid][0].get_data({"v_uid": "0222", "type": data["action"], "data": data})
            with open("static/files/{}".format(data["filename"]), "wb") as f:
                f.write(base64.b64decode(_data["data"]))
            return jsonify({"code": 0})
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": data["action"], "data": data})
        return jsonify({"code": 0, "data": _data["raw"]})

import json
from flask import Blueprint, request, render_template, jsonify
from config import SPEED, cache

shell = Blueprint('shell', __name__, template_folder=".")


@shell.route('/shell/<uid>', methods=['GET', 'POST'])
def __shell(uid):
    if request.method == "GET":
        return render_template('shell.html')
    else:
        _key = json.loads(request.data.decode())["data"]
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "shell", "data": _key})
        return jsonify(_data)

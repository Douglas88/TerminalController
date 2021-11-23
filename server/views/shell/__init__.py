import json
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

shell = Blueprint('shell', __name__, template_folder=".")


@shell.route('/shell/<uid>', methods=['GET', 'POST'])
def __shell(uid):
    if request.method == "GET":
        return render_template('shell.html')
    else:
        _key = json.loads(request.data.decode())["data"]
        _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": "shell", "data": _key})
        return jsonify(_data)

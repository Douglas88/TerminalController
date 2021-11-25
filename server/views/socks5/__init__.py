import json
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

socks5 = Blueprint('socks5', __name__, template_folder=".")


@socks5.route('/socks5/<uid>', methods=['GET', 'POST'])
def __socks5(uid):
    if request.method == "GET":
        return render_template('socks5.html')
    else:
        data = json.loads(request.data)
        with open("plugins/socks5.py", "r") as f:
            code = f.read().replace("127.0.0.1", data["host"]).replace("9011", data["port"]).replace("{username}", data["username"]).replace("{password}", data["password"])
            _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": data["type"], "code": code})
            return jsonify(_data)

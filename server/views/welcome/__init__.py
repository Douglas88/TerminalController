import json
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

welcome = Blueprint('welcome', __name__, template_folder=".")


@welcome.route('/welcome/<uid>', methods=['GET', 'POST'])
def __welcome(uid):
    if request.method == "GET":
        _code = request.args.get("code")
        print("[*] welcome", _code)
        _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": "code", "code": _code})
        return render_template('welcome.html', welcome=_data)

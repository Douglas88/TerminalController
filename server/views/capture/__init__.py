from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

capture = Blueprint('capture', __name__, template_folder=".")


@capture.route('/capture/<uid>', methods=['GET', 'POST'])
def __capture(uid):
    if request.method == "GET":
        return render_template('capture.html', speed=SPEED)
    else:
        _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": "capture"})
        return jsonify(_data)

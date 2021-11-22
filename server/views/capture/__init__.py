from flask import Blueprint, request, render_template, jsonify
from config import SPEED, cache

capture = Blueprint('capture', __name__, template_folder=".")


@capture.route('/capture/<uid>', methods=['GET', 'POST'])
def __capture(uid):
    if request.method == "GET":
        return render_template('capture.html', speed=SPEED)
    else:
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "capture"})
        return jsonify(_data)


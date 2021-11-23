import base64
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

key = Blueprint('key', __name__, template_folder=".")


@key.route('/key/<uid>', methods=['GET', 'POST'])
def __key(uid):
    _data = current_app.cache[uid][0].send_term_command({"v_uid": "0222", "type": "key"})
    code = base64.b64decode(_data["data"]).decode()
    return render_template('key.html', code=code)

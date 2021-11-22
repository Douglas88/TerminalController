import base64
from flask import Blueprint, request, render_template, jsonify
from config import SPEED, cache

key = Blueprint('key', __name__, template_folder=".")


@key.route('/key/<uid>', methods=['GET', 'POST'])
def __key(uid):
    _data = cache[uid][0].get_data({"v_uid": "0222", "type": "key"})
    code = base64.b64decode(_data["data"]).decode()
    return render_template('key.html', code=code)

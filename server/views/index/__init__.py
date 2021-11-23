import base64
import datetime
from flask import Blueprint, request, render_template, jsonify, current_app
from config import SPEED

index = Blueprint('index', __name__, template_folder=".")


@index.route('/')
def _index():
    return render_template('index.html')


@index.route('/api.json')
def _api():
    return jsonify({"code": 0, "data": [{"uid": i, "system": current_app.cache[i][1], "uptime": current_app.cache[i][2]} for i in current_app.cache.keys()]})
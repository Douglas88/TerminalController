from flask import Blueprint, request, render_template, jsonify
from config import SPEED
core = Blueprint('core', __name__, template_folder=".")


@core.route('/init')
def __core():
    """
    return client's code
    :return:
    """
    print("[*] Client connect <----", request.remote_addr)
    with open("plugins/core.py", "r", encoding="utf8") as f:
        return f.read()

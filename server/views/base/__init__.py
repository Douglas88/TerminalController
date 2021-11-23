from flask import Blueprint, request, render_template, jsonify
from config import SPEED
base = Blueprint('base', __name__, template_folder=".")


@base.route('/base')
def __base():
    """
    return client's code
    :return:
    """
    print("[*] Client connect <----", request.remote_addr)
    with open("plugins/base.py", "r", encoding="utf8") as f:
        return f.read()

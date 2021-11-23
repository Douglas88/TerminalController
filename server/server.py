import sys
import datetime
import json
from flask import Flask, current_app
from flask_sockets import Sockets
import time
from config import *
from model.msg import MSG
from views import *

app = Flask(__name__)
sockets = Sockets(app)
with app.app_context():
    current_app.cache = {}  # term Object


@sockets.route("/ping")
def ping(ws):
    msg = json.loads(ws.receive())
    uid = msg['uid']
    current_app.cache.update({uid: [MSG(ws), msg["system"], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]})
    while not ws.closed:
        try:
            ws.send('')
            time.sleep(3)
        except Exception as e:
            break
    current_app.cache.pop(uid)


for view in views:
    print("[*]", view.name, "router add success")
    app.register_blueprint(view)


if __name__ == '__main__':
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    from gevent import monkey

    monkey.patch_all()
    app.debug = True
    server = pywsgi.WSGIServer((HOST, PORT), app, handler_class=WebSocketHandler)
    print("server run at", "http://{}:{}".format(HOST, PORT))
    try:
        server.serve_forever()
    except KeyboardInterrupt as e:
        server.stop()
        sys.exit()

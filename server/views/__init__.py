
# from .index import index
# from .capture import capture
# from .edit import edit
# from .file import file
# from .key import key
# from .make import make
# from .shell import shell
# from .base import base
import os
import traceback
views = []


for _dir in os.listdir(os.path.dirname(__file__)):
    if _dir != "__pycache__" and os.path.isdir(os.path.join(os.path.dirname(__file__), _dir)):
        try:
            exec("from .{0} import {0};views.append({0})".format(_dir))
        except ImportError as e:
            print("[!] --------------------------------------------------------")
            traceback.print_exc()


import json
import threading


class MSG:
    def __init__(self, ws):
        """
        存放客户端，用于后期收发消息加锁
        :param ws:
        """
        self.lock = threading.RLock()
        self.ws = ws

    def send_term_command(self, data: dict) -> dict:
        """
        向终端发送指令
        """
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

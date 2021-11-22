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
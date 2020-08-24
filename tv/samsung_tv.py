import samsungctl
from tv.exceptions.tv_exceptions import TvNotConnected


class SamsungTV:
    """ Base class for Samsung APIs """

    def __init__(self,
                 name,
                 host,
                 port,
                 method,
                 timeout=0,
                 description="Samsung TV"):
        self.name = name
        self.host = host
        self.port = port
        self.method = method
        self.timeout = timeout
        self.description = description
        self.tv_remote = None

    def _generate_config(self):
        return {
            "name": self.name,
            "description": self.description,
            "id": "",
            "host": self.host,
            "port": self.port,
            "method": self.method,
            "timeout": self.timeout,
        }

    def _is_connected(self):
        if self.tv_remote is not None:
            return True
        else:
            return False

    def connect(self):
        if not self._is_connected():
            config = self._generate_config()
            self.tv_remote = samsungctl.Remote(config)

    def power(self):
        if self._is_connected():
            self.tv_remote.control("KEY_POWER")
        else:
            raise TvNotConnected("TV is Not Connected")

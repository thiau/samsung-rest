import samsungctl
import logging
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

        # Logging config
        self.log = logging.getLogger('samsung.rest')
        self.log.setLevel(logging.INFO)
        self.last_action = None

    def _get_action(self, action):
        actions = {"power": self.power, "volume_up": self.volume_up}
        return actions.get(action, None)

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

    def connect(self, force_connect=False):
        if not self._is_connected() or force_connect:
            config = self._generate_config()
            self.tv_remote = None
    def _retry_last_action(self):
        self.log.info("Will retry last action")

        # Reconnect
        self.disconnect()
        self.connect()

        action = self._get_action(action=self.last_action)

        if action is not None:
            action()
        else:
            self.log.info("Last action not found")

    def power(self):
        try:
            if self._is_connected():
                self.tv_remote.control("KEY_POWER")
            else:
                raise TvNotConnected("TV is Not Connected")
        except Exception as err:
            self.log.info("Some error occured. Will try to reconnect")
            self.log.info(err)
            self.connect(force_connect=True)

    def volume_up(self):
        try:
            if self._is_connected():
                self.tv_remote.control("KEY_VOLUP")
            else:
                raise TvNotConnected("TV is Not Connected")
        except Exception as err:
            self.log.info("Some error occured. Will try to reconnect")
            self.log.info(err)
            self.connect(force_connect=True)

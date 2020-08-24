import os
from flask import Flask
from dotenv import load_dotenv
from tv.samsung_tv import SamsungTV

load_dotenv()

app = Flask(__name__)

hostname = os.getenv("TV_HOSTNAME")
port = int(os.getenv("TV_PORT"))

samsung_tv = SamsungTV(
    name="SamsungTV", host=hostname, port=port, method="websocket")

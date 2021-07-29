import os

from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler

from app import app
import events

if __name__ == "__main__":
    load_dotenv()

    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

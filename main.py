import os
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

from app import app
from logger import logging
import events

if __name__ == "__main__":
    load_dotenv()
    logging.info("Started Slack Bot")

    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

import os

from dotenv import load_dotenv
from slack_bolt import App

load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

import os
import random

from dotenv import load_dotenv
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from typing import List

load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")


@app.event("app_mention")
def event_test(say):
    say("Hi there!")


@app.event("message")
def react_to_message(body, say, ack, client):
    ack()
    channel_id = body["event"]["channel"]
    event_ts = body["event"]["event_ts"]
    reactions = ["thumbsup", "thumbsdown"]
    reaction_name = random.choice(reactions)
    client.reactions_add(channel=channel_id, name=reaction_name, timestamp=event_ts)


@app.message("hello")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()

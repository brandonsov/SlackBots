import os
import random

from app import app
from logger import logging

ABDUL_USER_ID = "U0291SC0HLN"


@app.event("app_mention")
def event_test(say):
    say("Hi there!")


@app.event("message")
def react_to_message(body, say, ack, client):
    ack()

    logging.info(f"{body}")

    channel_id = body["event"]["channel"]
    event_ts = body["event"]["event_ts"]
    user_id = body["event"]["user"]
    reactions = {key.lower(): key for (key, _value)
                 in client.emoji_list()["emoji"].items()}
    text = body["event"]["text"]
    for word in text.split():
        cand = word.lower().strip(":")
        if cand in reactions:
            client.reactions_add(
                channel=channel_id, name=reactions[cand], timestamp=event_ts)
            reactions.pop(cand)

    if user_id == ABDUL_USER_ID:
        reaction_name = "triggered_parrot"
    else:
        reaction_name = random.choice(list(reactions.values()))
    chance = random.randint(0, 100)
    if chance / 100 < float(os.environ["EMOJI_FREQUENCY"]):
        client.reactions_add(channel=channel_id,
                             name=reaction_name, timestamp=event_ts)

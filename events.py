import os
import random

import requests

from app import app
from leetcode import get_random_leetcode_question
from logger import logging

ABDUL_USER_ID = "U0291SC0HLN"
LEETCODE_BASE_URL = "https://leetcode.com"
LEETCODE_API_ROUTE = "api/problems/all"
LEETCODE_DIFFICULTY = {1: "Easy", 2: "Medium", 3: "Hard"}


@app.event("app_mention")
def event_test(say):
    say("Hi there!")


@app.command("/leetcode")
def get_leetcode_question(ack, say):
    ack()

    if question := get_random_leetcode_question():
        say(
            f"Name: {question.name}\n"
            f"Difficulty: {question.difficulty}\n"
            f"Link: {question.url()}")
    else:
        say("Unable to get Leetcode Question")


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

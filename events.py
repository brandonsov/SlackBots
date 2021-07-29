import random

from app import app

ABDUL_USER_ID = "U0291SC0HLN"


@app.event("app_mention")
def event_test(say):
    say("Hi there!")


@app.event("message")
def react_to_message(body, say, ack, client):
    ack()
    print(f"{body}")
    channel_id = body["event"]["channel"]
    event_ts = body["event"]["event_ts"]
    reactions = client.emoji_list()["emoji"]
    user_id = body["event"]["user"]
    text = body["event"]["text"]
    words = text.split()
    for word in words:
        if word in reactions.keys():
            reactions.pop(word)
            client.reactions_add(channel=channel_id, name=word, timestamp=event_ts)

    try:
        client.reactions_add(channel=channel_id, name=text, timestamp=event_ts)
    except:
        pass

    if user_id == ABDUL_USER_ID:
        reaction_name = "triggered_parrot"
    else:
        reaction_name = random.choice(list(reactions.keys()))
    client.reactions_add(channel=channel_id, name=reaction_name, timestamp=event_ts)

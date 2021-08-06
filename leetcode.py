import random

import requests
from logger import logging


LEETCODE_BASE_URL = "https://leetcode.com"
LEETCODE_API_ROUTE = "api/problems/all"
LEETCODE_DIFFICULTY = {1: "Easy", 2: "Medium", 3: "Hard"}


class LeetcodeQuestion():
    def __init__(self, name, question_title_slug, difficulty):
        self.name = name
        self.question_title_slug = question_title_slug
        self.difficulty = LEETCODE_DIFFICULTY[difficulty]

    def url(self):
        return f"{LEETCODE_BASE_URL}/problems/{self.question_title_slug}/"


def get_random_leetcode_question():
    r = requests.get(f"{LEETCODE_BASE_URL}/{LEETCODE_API_ROUTE}/")
    if r.status_code != 200 or not r.json():
        logging.error(f"Failed to get Leetcode problem, {r.text()}")
        return

    # Could deserialize into LeetcodeQuestion objects here
    result = r.json()["stat_status_pairs"]
    questions = list(filter(lambda x: not x["paid_only"], result))
    question = random.choice(questions)

    return LeetcodeQuestion(
        question["stat"]["question__title"],
        question["stat"]["question__title_slug"],
        question["difficulty"]["level"]
    )

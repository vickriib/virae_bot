import json
import random

def load_cards():
    with open('data/cards.json', 'r') as file:
        return json.load(file)

CARDS = load_cards()

def get_random_card():
    return random.choice(CARDS)

def get_card_by_id(card_id):
    for card in CARDS:
        if card['id'] == card_id:
            return card
    return None

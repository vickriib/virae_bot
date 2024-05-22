import json

def load_user_data():
    try:
        with open('data/users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(data):
    with open('data/users.json', 'w') as file:
        json.dump(data, file)

def add_card_to_collection(user_id, card):
    data = load_user_data()
    if str(user_id) not in data:
        data[str(user_id)] = []
    data[str(user_id)].append(card)
    save_user_data(data)

def get_user_collection(user_id):
    data = load_user_data()
    return data.get(str(user_id), [])

def trade_card(from_user_id, to_user_id, card_id):
    data = load_user_data()
    from_user_collection = data.get(str(from_user_id), [])
    to_user_collection = data.get(str(to_user_id), [])

    card_to_trade = None
    for card in from_user_collection:
        if card['id'] == card_id:
            card_to_trade = card
            break

    if card_to_trade:
        from_user_collection.remove(card_to_trade)
        to_user_collection.append(card_to_trade)
        save_user_data(data)
        return True
    return False


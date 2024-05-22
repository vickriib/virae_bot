import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
from cards import get_random_card, get_card_by_id
from collections import add_card_to_collection, get_user_collection, trade_card
from groups import search_groups

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("7119919089:AAF1c2W1J0INhJZy5LP7NwuNJ0ziIz4ZlKM")

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    # Adicione mais handlers conforme necessário

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    context.user_data['cards'] = []
    update.message.reply_text(f'Olá, {user.first_name}! Bem-vindo ao Viraê!')

def virar(update: Update, context: CallbackContext) -> None:
    card = get_random_card()
    add_card_to_collection(update.effective_user.id, card)
    update.message.reply_text(f'Você recebeu a carta: {card["name"]} da categoria {card["category"]}')

def coleção(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    user_collection = get_user_collection(user_id)
    if not user_collection:
        update.message.reply_text('Você não possui nenhuma carta na sua coleção.')
        return

    cards_text = "\n".join([f"{card['id']}: {card['name']} ({card['category']})" for card in user_collection])
    update.message.reply_text(f'Sua coleção:\n{cards_text}')

def trade(update: Update, context: CallbackContext) -> None:
    # Implementação da lógica de troca de cartas
    pass

def search_group(update: Update, context: CallbackContext) -> None:
    query = " ".join(context.args)
    groups = search_groups(query)
    if not groups:
        update.message.reply_text('Nenhum grupo encontrado.')
        return
    
    groups_text = "\n".join([f"{group['id']}: {group['name']}" for group in groups])
    update.message.reply_text(f'Grupos encontrados:\n{groups_text}')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('virar', virar))
    dispatcher.add_handler(CommandHandler('coleção', coleção))
    dispatcher.add_handler(CommandHandler('trade', trade))
    dispatcher.add_handler(CommandHandler('search_group', search_group))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from cards import get_random_card
from collections import add_card_to_collection, get_user_collection, trade_card
from groups import search_groups

# Configuração de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Obter o token do bot a partir das variáveis de ambiente
TOKEN = os.getenv("7119919089:AAF1c2W1J0INhJZy5LP7NwuNJ0ziIz4ZlKM")

if not TOKEN:
    raise ValueError("O TOKEN do bot não está configurado nas variáveis de ambiente.")

def start(update:Update, context:CallbackContext) -> None:
    user = update.effective_user
    context.user_data['cards'] = []
    update.message.reply_text(f'Olá, {user.first_name}! Bem-vindo ao bot de colecionar cartas!')

def main() -> None:
    # Verificar se o TOKEN está definido
    if not TOKEN:
        logging.error("O TOKEN do bot não está definido.")
        return

    # Criar o Updater e passar o TOKEN do bot
    updater = Updater(TOKEN)

    # Obter o dispatcher para registrar os handlers
    dispatcher = updater.dispatcher

    # Adicionar o comando /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Iniciar o bot
    updater.start_polling()

    # Executar o bot até que o processo seja interrompido
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

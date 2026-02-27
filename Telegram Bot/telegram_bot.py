from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import telegram.ext.filters as filters
import os
import bitsgpt_tele  # Import your "bitsgpt_tele.py" chatbot logic

def start(update, context):
    update.message.reply_text("Hello! I'm your chatbot. Send me a message.")

def handle_message(update, context):
    user_input = update.message.text
    response = bitsgpt_tele.handle_user_input(user_input)  # Call your chatbot function
    update.message.reply_text(response)

def main():
    # Initialize the Telegram Bot
    updater = Updater(token=os.environ['6957597341:AAELv2pvBrTzCCpfMQDmUIKM8uy_6_Nxk8I'], use_context=True)
    dp = updater.dispatcher

    # Create a command handler for the /start command
    dp.add_handler(CommandHandler('start', start))

    # Create a message handler for handling all other text messages
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()  
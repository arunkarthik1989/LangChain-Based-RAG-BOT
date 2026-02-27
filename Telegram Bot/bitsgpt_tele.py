from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
import telegram.ext.filters as filters
import os
import constants
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Initialize the index and chat model
loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])
chat_model = ChatOpenAI()

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm your chatbot. Send me a message.")

def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text

    # Use your chatbot logic to generate a response
    response = index.query(user_input, llm=chat_model)

    update.message.reply_text(response)

def main():
    # Initialize the Telegram Bot
    updater = Updater(token='6957597341:AAELv2pvBrTzCCpfMQDmUIKM8uy_6_Nxk8I', use_context=True)
    dp = updater.dispatcher

    # Create a command handler for the /start command
    dp.add_handler(CommandHandler('start', start))
    
    # Create a message handler for handling all other text messages
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

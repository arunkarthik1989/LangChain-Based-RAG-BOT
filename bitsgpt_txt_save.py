import os
import logging
import sys
from datetime import datetime
import constants
from langchain.document_loaders import TextLoader 
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Set up logging
log_file_path = 'question_log.txt'
logging.basicConfig(filename=log_file_path, level=logging.INFO)

os.environ["OPENAI_API_KEY"] = constants.APIKEY

def get_user_details():
    # Ask for Username and Bits ID
    username = input("Enter your Username: ")
    bits_id = input("Enter your Bits ID: ")

    # Log user information
    user_info_message = f"User Information - Username: {username}, Bits ID: {bits_id}"
    logging.info(user_info_message)

    return username, bits_id

def run_chatbot(username, bits_id):
    while True:
        # Ask the user for a question
        query = input("Ask the chatbot (type 'exit' to end): ")
        if query.lower() == 'exit':
            break

        # Log the question along with user information
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} - {username} (Bits ID: {bits_id}) asked: {query}"
        logging.info(log_message)

        # Continue with the rest of the code
        loader = TextLoader('data.txt')
        index = VectorstoreIndexCreator().from_loaders([loader])

        response = index.query(query, llm=ChatOpenAI())
        print(response)

if __name__ == "__main__":
    # Get user details
    username, bits_id = get_user_details()

    # Run the chatbot loop
    run_chatbot(username, bits_id)

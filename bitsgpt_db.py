import os
import logging
from datetime import datetime
import mysql.connector
from langchain.document_loaders import TextLoader 
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import constants

# Set up logging
log_file_path = 'question_log.txt'
logging.basicConfig(filename=log_file_path, level=logging.INFO)

# MySQL connection configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Reset123',
    'database': 'dbforchatbot',
}

os.environ["OPENAI_API_KEY"] = constants.APIKEY

def insert_into_database(username, bits_id, query):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_query = "INSERT INTO data (datetime, username, userid, questions) VALUES (%s, %s, %s, %s)"
        data = (current_time, username, bits_id, query)
        cursor.execute(insert_query, data)

        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def run_chatbot(username, bits_id, question):
    try:
        loader = TextLoader('data.txt')
        index = VectorstoreIndexCreator().from_loaders([loader])

        response = index.query(question, llm=ChatOpenAI())
        insert_into_database(username, bits_id, question)  # Insert question into the database
        return response
    except Exception as e:
        return f"Error: {e}"

# If you want to run the chatbot script independently for testing:
if __name__ == "__main__":
    # Get user details (for testing purposes)
    username = input("Enter your Username: ")
    bits_id = input("Enter your Bits ID: ")

    # Ask a question (for testing purposes)
    question = input("Ask the chatbot: ")

    # Run the chatbot and print the response
    response = run_chatbot(username, bits_id, question)
    print(response)

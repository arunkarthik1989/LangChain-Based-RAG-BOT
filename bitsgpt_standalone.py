from datetime import datetime
from langchain.document_loaders import TextLoader 
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
import constants
import os

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = constants.APIKEY

def run_chatbot(question):
    try:
        # Assuming 'data.txt' contains training data for the chatbot
        loader = TextLoader('data.txt')
        index = VectorstoreIndexCreator().from_loaders([loader])

        # Use ChatOpenAI model for generating responses
        response = index.query(question, llm=ChatOpenAI())

        return response
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        # Ask a question (for testing purposes)
        question = input("Ask the chatbot (type 'exit' to quit): ")

        if question.lower() == 'exit':
            break  # Exit the loop if the user types 'exit'

        # Run the chatbot and print the response
        response = run_chatbot(question)
        print(response)

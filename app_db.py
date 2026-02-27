from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Dictionary to store user information
user_info = {}

@app.route('/')
def home():
    return render_template('chat_db.html')

@app.route('/set_user_info', methods=['POST'])
def set_user_info():
    data = request.get_json()

    username = data.get('username', 'DefaultUsername')
    bits_id = data.get('bits_id', 'DefaultBitsID')

    # Store user information in the dictionary
    user_info['username'] = username
    user_info['bits_id'] = bits_id

    return jsonify({'status': 'success'})

@app.route('/get', methods=['POST'])
def get_response():
    data = request.get_json()

    user_message = data.get('msg', '')

    # Retrieve user information from the stored dictionary
    username = user_info.get('username', 'DefaultUsername')
    bits_id = user_info.get('bits_id', 'DefaultBitsID')

    # Log user information
    user_info_message = f"User Information - Username: {username}, Bits ID: {bits_id}"
    print(user_info_message)

    try:
        # Use Flask's __file__ to get the current script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        bitsgpt_path = os.path.join(script_dir, 'bitsgpt_db1.py')

        # Run the chatbot script (bitsgpt.py) using subprocess
        result = subprocess.run(['python', bitsgpt_path], input=user_message, capture_output=True, text=True, check=True, cwd=script_dir, env={'USERNAME': username, 'BITS_ID': bits_id})

        # Get the chatbot's response from the script's standard output
        bot_response = result.stdout
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here, such as if the script returns a non-zero exit code
        bot_response = f"Error: {e.stderr}"

    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)

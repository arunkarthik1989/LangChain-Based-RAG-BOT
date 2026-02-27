from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/get', methods=['POST'])
def get_response():
    user_message = request.form["msg"]

    try:
        # Send the user's message to the chatbot script (bitsgpt.py) and capture the output
        result = subprocess.run(['python', 'bitsgpt.py', user_message], capture_output=True, text=True, check=True)

        # Get the chatbot's response from the script's standard output
        bot_response = result.stdout
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions here, such as if the script returns a non-zero exit code
        bot_response = f"Error: {e.stderr}"
    print(bot_response)    

    return jsonify(bot_response)

if __name__ == '__main__':
    # Bind to the specific public IP address and port 5000
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

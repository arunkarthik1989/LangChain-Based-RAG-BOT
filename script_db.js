function getUserInfo() {
    var username = document.getElementById("username").value;
    var bitsId = document.getElementById("bits-id").value;

    // Send the user information to the server
    $.ajax({
        type: 'POST',
        url: '/set_user_info',
        data: { 'username': username, 'bits_id': bitsId },
        success: function(response) {
            // Display a success message or handle the response as needed
            console.log('User information submitted successfully');
        },
        error: function(error) {
            // Handle errors or display an error message
            console.error('Error submitting user information', error);
        }
    });
}

function sendMessage() {
    var userMessage = document.getElementById("user-message").value;

    // Send the user's message to the server
    $.ajax({
        type: 'POST',
        url: '/get',
        data: { 'msg': userMessage },
        success: function(response) {
            // Display the chatbot's response
            document.getElementById("chat-container").innerHTML += '<p>User: ' + userMessage + '</p>';
            document.getElementById("chat-container").innerHTML += '<p>Chatbot: ' + response.bot_response + '</p>';
        },
        error: function(error) {
            // Handle errors or display an error message
            console.error('Error getting chatbot response', error);
        }
    });

    // Clear the input field after sending the message
    document.getElementById("user-message").value = '';
}

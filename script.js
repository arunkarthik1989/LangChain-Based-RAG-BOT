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
            document.getElementById("chat-container").innerHTML += '<p>Chatbot: ' + response.response + '</p>';
        },
        error: function(error) {
            // Handle errors or display an error message
            console.error('Error getting chatbot response', error);
        }
    });

    // Clear the input field after sending the message
    document.getElementById("user-message").value = '';
}

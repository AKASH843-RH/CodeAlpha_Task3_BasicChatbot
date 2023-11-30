# Define a dictionary with patterns and corresponding responses
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you?": "I'm good, thank you.",
    "yours developer is":"my developer is akash.",
    "what's your name?": "I'm a chatbot.",
    "bye": "Goodbye!",
    "tell me about yourself": ["I'm just a simple chatbot created to chat with people.", "I'm here to assist and have conversations with you!"],
    "what's the weather like today?": ["I'm sorry, I don't have access to real-time weather information."],
    "default": ["I'm not sure about that.", "I'm still learning!"]
}
    
# Function to get appropriate response based on user input
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the input matches any predefined patterns
    for pattern, response in responses.items():
        if pattern in user_input:
            return response

    # If no match is found, return the default response
    return responses['default']

# Function to handle the conversation
def chat():
    print("Chatbot: Hi! Let's chat. Type 'bye' to exit.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

# Start the chat
if __name__ == "__main__":
    chat()
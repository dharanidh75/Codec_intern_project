import re

def get_response(user_input):
    user_input = user_input.lower()
    
    # Rule-based dictionary
    rules = {
        r".*(hello|hi|hey).*": "Hello! Welcome to our support center. How can I help you today?",
        r".*(status|track).*order.*": "To track your order, please visit our tracking page with your Order ID.",
        r".*refund|return.*": "Our return policy allows refunds within 30 days of purchase. Would you like a link to the return form?",
        r".*business hours|open.*": "We are open Monday to Friday, 9 AM to 6 PM EST.",
        r".*(bye|goodbye).*": "Thank you for reaching out! Have a great day.",
    }
    
    for pattern, response in rules.items():
        if re.match(pattern, user_input):
            return response
            
    return "I'm sorry, I didn't quite understand that. Could you please rephrase or ask for a human agent?"

def start_chat():
    print("🤖 Customer Support Bot (Type 'exit' to end)")
    print("-" * 40)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bot: Goodbye!")
            break
        print("Bot:", get_response(user_input))

if __name__ == "__main__":
    start_chat()

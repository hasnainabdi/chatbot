import openai

# Set your OpenAI API key
openai.api_key = "sk-AdfvF87c9Tyqf9UqacUCT3B1bkFJbAEj8ZeepiDsBkwubggl"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

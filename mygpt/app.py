import openai

openai.api_key = "sk-AdfvF87c9Tyqf9UqacUCT3B1bkFJbAEj8ZeepiDsBkwubggl"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     messages=[{"role": "user", "content": prompt}]
         )
         
         return response.choices[0].message.content.strip()
         
         if_name=="main_":
             while True:
                 user_input = input("You: ")
                 user_input = input.lower() in ["quit", "exit", "bye"]:
                     break
                     
                     response = chat_with_gpt(user_input)
                     print("Chatbot: ", response)
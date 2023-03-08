import openai
from dotenv import load_dotenv
import os
load_dotenv(".env.local")

openai.api_key = os.getenv("OPENAI_API_KEY")

class Bot:
    def __init__(self):
        self.messages=[]

    def new_message(self, role, content):
        self.messages.append({'role': role, 'content': content})


    def get_response(self):
        output = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            temperature=0.5
        )
        response = output['choices'][0]['message']['content']

        self.messages.append({'role': 'assistant', 'content': response})

        return response



def main():
    role = 'user'
    bot = Bot()
    while True:
        inp = input('You: ')
        if inp == 'q':
            break

        if inp == 'response':
            res = bot.get_response()
            print('Bot:', res)
            continue
        bot.new_message(role, inp)

if __name__ == '__main__':
    main()
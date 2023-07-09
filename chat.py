#!/usr/bin/env python

import argparse
import os
import openai
import json

from dotenv import load_dotenv

CODEBASE_DIRECTORY = '/Users/hendrikgobel/code/java/workspace/cards/src/cards'

load_dotenv()

def main():

    conversation = load_conversation_history()
    prompt = request_input()
    conversation.append(prompt)
    response = init_openai(conversation)
    
    result = response.choices[0].message['content']
    print(result)
    

def load_conversation_history():
    conversation_file = 'conversation_history.json'
    try:
        with open(conversation_file, 'r') as file:
            conversation = json.load(file)
    except FileNotFoundError:
        conversation = init_conversation(load_codebase())
    return conversation

def init_conversation(codebase):
     
     return [
            {"role": "system", "content": "you are a code reviewer who reviews the code and gives suggestions for avoiding bugs, improving code style, enhancing security, increasing efficiency, improving readability, and making other possible improvements."},
            {"role": "user", "content": codebase},
        ]

def init_openai(messages):
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response
  
def request_input():  
    parser = argparse.ArgumentParser(description='GPT Command-Line Tool')
    parser.add_argument('prompt', help='Your question?')
    args = parser.parse_args()
    return {"role": "user", "content": args.prompt}

def generate_prompt(animal):
    return f"""Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {animal.capitalize()}
Names:"""


def load_codebase():
    
    codebase_directory = os.getenv("PATH_TO_CODEBASE")

    # List to store the encoded codebase
    encoded_codebase = []

    # Recursively iterate through the codebase directory
    for root, _, files in os.walk(codebase_directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file_obj:
                file_content = file_obj.read()
                # Encode or process the file_content as needed
                encoded_codebase.append(file_content)


    codebase_string = '\n'.join(encoded_codebase)
    
    return codebase_string            

if __name__ == '__main__':
    main()

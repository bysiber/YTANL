import json

def read_json(file):
    with open(file, mode="r", encoding="utf-8") as f:
        return json.load(f)


VALUE_NAMES = ['message_type', 'occurence_timestamp', 'timeStampUTC', 'author', 'content']
DEFAULT_MSG_TYPE = "Chat Message"



all_chat = read_json("testj.json")

for message in all_chat:
    if message["message_type"] == DEFAULT_MSG_TYPE:
        for value in VALUE_NAMES:
            print(message[value])
        input("------------------------------------------")
    
    

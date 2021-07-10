# Import the required libraries
import os
import json
from gitterpy.client import GitterClient
from . import data_extraction

# Take config variables from the .env file of the project
ROOM_ID = os.getenv('ROOM_ID')
TOKEN = os.getenv('TOKEN')
room = os.getenv('room')
CHATBOT_NAME = os.getenv('CHATBOT_NAME')

# Communicate with the Gitter channel (send and listen messages)
gitter = GitterClient(TOKEN)

response = gitter.stream.chat_messages(room)
for stream_messages in response.iter_lines():
    if len(stream_messages) > 10:
        parsed_message = json.loads(stream_messages.decode('utf-8'))
        message_sender = parsed_message["fromUser"]["username"]
        message = parsed_message["text"]
        if message.startswith('@bot -help'):
            BOTANSWER = "**chatbot** I am currently learning this feature try after some time!"
            gitter.messages.send(room, BOTANSWER)
        elif not message.startswith('**chatbot**'):
            BOTANSWER = data_extraction.processMessageL1(message.lower(), message_sender)
            if BOTANSWER != -1:
                gitter.messages.send(room, BOTANSWER)

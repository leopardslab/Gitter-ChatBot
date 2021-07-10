# Import the required libraries
from gitterpy.client import GitterClient
import json
import os
import data_extraction

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
            botanswer = "**chatbot** I am currently learning this feature try after some time!"
            gitter.messages.send(room, botanswer)
        elif not message.startswith('**chatbot**'):
            botanswer = data_extraction.processMessageL1(message.lower(), message_sender)
            if botanswer != -1:
                gitter.messages.send(room, botanswer)

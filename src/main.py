import os
import json
from gitterpy.client import GitterClient
from dotenv import load_dotenv
import data_extraction
import response

def chat_bot():
    # Load the config variables
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    ROOM = os.getenv('ROOM')
    CHATBOT_NAME = os.getenv('CHATBOT_NAME')

    # Communicate with the Gitter channel (send and listen messages)
    gitter = GitterClient(TOKEN)

    res = gitter.stream.chat_messages(ROOM)
    for stream_messages in res.iter_lines():
        if len(stream_messages) > 10:
            parsed_message = json.loads(stream_messages.decode('utf-8'))
            message_sender = parsed_message["fromUser"]["username"]
            message = parsed_message["text"]
            if message.startswith('@' + CHATBOT_NAME):
                BOTANSWER = "**{}** I am currently learning this feature try after some time.".format(CHATBOT_NAME)
                gitter.messages.send(ROOM, BOTANSWER)
            elif not message.startswith('**{}**'.format(CHATBOT_NAME)):
                __data__ = data_extraction.process_message(message.lower())
                if __data__ == [-1]:
                    pass
                    # Do noting
                elif __data__ == [0]:
                    BOTANSWER = response.default_suggestion_answer(message_sender)
                    gitter.messages.send(ROOM, BOTANSWER)
                else:
                    BOTANSWER = response.project_suggestion_answer(message_sender,__data__)
                    gitter.messages.send(ROOM, BOTANSWER)

if __name__ == "__main__":
    chat_bot()

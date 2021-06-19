# Import the required libraries
from gitterpy.client import GitterClient
import json
import os
from dotenv import load_dotenv

# Take config variables from the .env file of the project
load_dotenv()
ROOM_ID = os.getenv('ROOM_ID')
TOKEN = os.getenv('TOKEN')
room = os.getenv('room')
CHATBOT_NAME = os.getenv('CHATBOT_NAME')

# Store some information about the community
about_community = os.getenv('ABOUT_COMMUNITY')
community_website_link = os.getenv('COMMUNITY_WEBSITE')
community_github_link = os.getenv('COMMUNITY_GITHUB')


# Create some demonstration information
class Project:
    def __init__(self, programming_lang, name, github_repo, gitter):
        self.programming_lang = programming_lang
        self.name = name
        self.github_repo = github_repo
        self.gitter = gitter


p1 = Project(["javascript", "python", "flask"], "ChatBot",
             "https://www.github.com", "https://www.gitter.com")

demonstartion_data = {p1}


# Function to process the message and extract the required information given by the user
def processMessageL1(query, username):
    count = 0
    user_skills = []
    introduction = {
        'study', 'undergraduate', 'fresher', 'year', 'university', 'new',
        'contributer', 'sophomore', 'open-source.', 'open source',
        'open-source', 'want to contribute', 'how to start', 'start', 'advice',
        'guide', 'scorelab', 'score-lab', 'projects on', 'projects based on',
        'how should i start', 'how to begin', 'how can i start',
        'how should i start', 'how should i proceed'
    }

    skills = {
        'css', 'html', 'javascript', 'python', 'react', 'django', 'flask',
        'mongodb', 'sql', 'mysql', 'shell'
    }

    for x in introduction:
        if x in query:
            count += 1

    if count > 2:
        for x in skills:
            if x in query:
                user_skills.append(x)
        if len(user_skills) != 0:
            for y in demonstartion_data:
                if user_skills[0] in y.programming_lang:
                    return '**chatbot**- Welcome @{} to scorelab community!\nI have found some projects which might interest you.\n- {} [Github]({}) [Gitter]({})'.format(
                        username, y.name, y.github_repo, y.gitter)
        return '**chatbot**- Welcome @{} to scorelab!\nI am ChatBot and I am here to answer your queries. \n**type `@bot -help` to learn more about me.**'.format(
            username)
    return "**chatbot** I am learning this"


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
            botanswer = processMessageL1(message.lower(), message_sender)
            gitter.messages.send(room, botanswer)

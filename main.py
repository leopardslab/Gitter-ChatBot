# Import the required libraries
from gitterpy.client import GitterClient
import json
import os
from dotenv import load_dotenv
import pymongo

# Take config variables from the .env file of the project
load_dotenv()
ROOM_ID = os.getenv('ROOM_ID')
TOKEN = os.getenv('TOKEN')
room = os.getenv('room')
CHATBOT_NAME = os.getenv('CHATBOT_NAME')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
CONNECTION_STRING = os.getenv('CONNECTION_STRING')

# Store some information about the community
about_community = os.getenv('ABOUT_COMMUNITY')
community_website_link = os.getenv('COMMUNITY_WEBSITE')
community_github_link = os.getenv('COMMUNITY_GITHUB')

# Database
# Provide the mongodb atlas url to connect python to mongodb using pymongo
client = pymongo.MongoClient(CONNECTION_STRING)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Store some demonstration information
# project1 = {
#     "tags": ["python", "shell", "machine learning", "ml"],
#     "name":
#     "Gitter-ChatBot",
#     "github-link":
#     "https://github.com/leopardslab/Gitter-ChatBot",
#     "gitter-link":
#     "https://gitter.im/LeaopardLabs/Gitter-ChatBot",
#     "good-first-issues":
#     "https://github.com/leopardslab/Gitter-ChatBot/labels/good%20first%20issue"
# }

# collection.insert_one(project1)

# Query the database for projects and interests, to find some projects
# def find_projects(queries):
#     for q in queries:
#         projects = collection.find({"tags": query})
#     return project
# for x in all_projects:
# print(x)


# Create a bot's answer when no skill is given by the user
def default_suggestion_answer(username):
    ans = "**chatbot** Hey @{}, really nice to have you here. I would be more than happy to help you throughout your contribution journey.\n".format(
        username)
    ans += "Can you tell me more about your skills and interests, so that I could suggest you some beginner level issues based on projects that uses your programming languages and fall in your interest.\n"
    ans += "You can do this by typing `@chatbot <programming language(s) here without chevrons>`\n"
    ans += "To learn more about me type `@chatbot -help`.\n Keep contributing and ask for help wherever you need."
    return ans


# Create a bot's answer when user gives their skills or interests
def project_suggestion_answer(username, queries):
    projects = []
    ans = "**chatbot** Hey @{}, really nice to have you here. I would be more than happy to help you throughout your contribution journey.\n".format(
        username)
    ans += "I have listed your skills and interests - {}\n".format(queries)

    for q in queries:
        res = collection.find({"tags": q}, {"_id": 0, "tags": 0})
        for project in res:
            if project not in projects:
                projects.append(project)

    if len(projects) == 0:
        ans += "Sorry " + username + ", I didn't find any projects matching your skills and interests :("
    else:
        ans += "I have found few projects for you :)\n"
    for p in projects:
        ans += "- {} [Github repository]({}) [Gitter channel]({}) [good first issues]({})\n".format(
            p['name'], p['github-link'], p['gitter-link'],
            p['good-first-issues'])

    return ans


# Function to process the message and extract the required information given by the user
def processMessageL1(message, username):
    count = 0
    queries = []
    introduction = {
        'study', 'undergraduate', 'fresher', 'year', 'university', 'new',
        'how can i contribute', 'opensource', 'like to contribute',
        'wish to contribute', 'contribute', 'contribute to scorelab',
        'can i contribute', 'scorelab', 'start contributing', 'college',
        'student', 'contributor', 'sophomore', 'open-source.', 'open source',
        'mentornship', 'get started', 'help', 'helpful', 'open-source',
        'want to contribute', 'how to start', 'start', 'advice', 'guide',
        'college', 'scorelab', 'score-lab', 'projects on', 'projects based on',
        'how should i start', 'how to begin', 'contibute', 'how can i start',
        'how should i start', 'how should i proceed', 'beginner',
        'how should i contribute', 'how can i get started'
    }

    skills = {
        'css', 'html', 'javascript', 'python', 'react', 'django', 'flask',
        'mongodb', 'sql', 'mysql', 'shell', 'mern', 'vue', 'node', 'express',
        'android', 'mobile', 'blockchain', 'web', 'c++', 'cpp', 'sql', 'mysql',
        'git', 'aws', 'golang', 'go'
    }

    interests = {
        'machine learning', 'ml', 'computer vision', 'deep learning', 'dl',
        'web development', 'web', 'android development', 'android', 'mobile',
        'computer vision'
    }

    if (message.startswith('@bot -p')):
        count = 3

    for x in introduction:
        if count > 2: break
        if x in message:
            count += 1

    if count > 2:
        for x in skills:
            if x in message:
                queries.append(x)
        for x in interests:
            if x in message:
                queries.append(x)
        if len(queries) != 0:
            return project_suggestion_answer(username, queries)
        return default_suggestion_answer(username)
    return -1


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
            if botanswer != -1:
                gitter.messages.send(room, botanswer)

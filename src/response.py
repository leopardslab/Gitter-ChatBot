import os
from dotenv import load_dotenv
import database

# Load required information about the community
load_dotenv()
CHATBOT_NAME = os.getenv('CHATBOT_NAME')
ORGANIZATION_GITHUB_NAME = os.getenv('ORGANIZATION_GITHUB_NAME')
ABOUT_COMMUNITY = os.getenv('ABOUT_COMMUNITY')
COMMUNITY_WEBSITE = os.getenv('COMMUNITY_WEBSITE')
COMMUNITY_GITHUB = os.getenv('COMMUNITY_GITHUB')
COMMUNITY_MAILING_LIST = os.getenv('COMMUNITY_MAILING_LIST')

#ChatBot help answer
def help_answer(username):
    ans = "**{}** Hey @{}, welcome to scorelab. I am a Gitter-ChatBot for this channel.\n".format(
        CHATBOT_NAME, username)
    ans += "I am programmed to guide new contributors by finding and listing all the community projects here.\n"    
    ans += "Suported commands:\n"    
    ans += "- `{} -help`, quick guide to Gitter-ChatBot. \n".format(CHATBOT_NAME)    
    ans += "- `{} -p`, list all the projects in given programming languages.\n".format(CHATBOT_NAME)    
    ans += "I listen to every message in the chat and appear whenever someone needs me :)"    
    
    return ans


#ChatBot's response when neither skills nor interests are given by the user
def default_suggestion_answer(username):
    ans = "**{}** Hey @{}, really nice to have you here. ".format(
        CHATBOT_NAME, username)
    ans += "I will be more than happy to help you throughout your contribution journey at {}.\n".format(
        ORGANIZATION_GITHUB_NAME)
    ans += "Can you tell me more about your skills and interests? "
    ans += "I will suggest you some projects and beginner level issues based on them.\n"
    ans += "You can do this by typing `@{} -p <name of your skills/interests>` eg. `@{} -p javascript python`.\n".format(
        CHATBOT_NAME, CHATBOT_NAME)
    ans += "To learn more about me type `@{} -help`.\n".format(CHATBOT_NAME)
    ans += "Keep contributing and ask for help wherever you need :)"
    return ans


#ChatBot's response when user provides atleast one of skills or interests
def project_suggestion_answer(username, queries):
    projects = []
    ans = "**{}** Hey @{}, really nice to have you here. ".format(
        CHATBOT_NAME, username)
    ans += "I will be more than happy to help you throughout your contribution journey.\n"
    ans += "I have listed your skills/interests - {}\n".format(queries)

    for _q_ in queries:
        res = database.collection.find({"tags": _q_}, {"_id": 0, "tags": 0})
        for project in res:
            if project not in projects:
                projects.append(project)

    if len(projects) == 0:
        ans += username + ", currently we don't have any project in these technologies.\n"
        ans += "You can checkout other projects of {} [here]({}).".format(
            ORGANIZATION_GITHUB_NAME, COMMUNITY_GITHUB)
    else:
        ans += "I have found few projects for you :)\n"
    for _p_ in projects:
        ans += "- {} [Github repository]({}) [Gitter channel]({}) [good first issues]({})\n".format(
            _p_['name'], _p_['github-link'], _p_['gitter-link'],
            _p_['good-first-issues'])

    return ans

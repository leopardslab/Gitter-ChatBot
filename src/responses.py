# Import database configurations and helper functions
import os
from . import database

# Store some information about the community
about_community = os.getenv('ABOUT_COMMUNITY')
community_website_link = os.getenv('COMMUNITY_WEBSITE')
community_github_link = os.getenv('COMMUNITY_GITHUB')


# Create a bot's answer when no skill is given by the user
def default_suggestion_answer(username):
    ans = "**chatbot** Hey @{}, really nice to have you here.\n".format(
        username)
    ans += "I would be more than happy to help you throughout your contribution journey.\n"
    ans += "Can you tell me more about your skills and interests?\n"
    ans += "I will suggest you some beginner level issues based on your skills and interest.\n"
    ans += "You can do this by typing `@chatbot <programming language(s) here without chevrons>`\n"
    ans += "To learn more about me type `@chatbot -help`.\n"
    ans += "Keep contributing and ask for help wherever you need."
    return ans


# Create a bot's answer when user gives their skills or interests
def project_suggestion_answer(username, queries):
    projects = []
    ans = "**chatbot** Hey @{}, really nice to have you here.\n".format(
        username)
    ans += "I will be more than happy to help you throughout your contribution journey.\n"
    ans += "I have listed your skills and interests - {}\n".format(queries)

    for _q_ in queries:
        res = database.collection.find({"tags": _q_}, {"_id": 0, "tags": 0})
        for project in res:
            if project not in projects:
                projects.append(project)

    if len(projects) == 0:
        ans += "@" + username + ", currently we don't have any project in these technologies.\n"
        ans += "You can check other projects [here]({}).".format(
            community_github_link)
    else:
        ans += "I have found few projects for you :)\n"
    for _p_ in projects:
        ans += "- {} [Github repository]({}) [Gitter channel]({}) [good first issues]({})\n".format(
            _p_['name'], _p_['github-link'], _p_['gitter-link'],
            _p_['good-first-issues'])

    return ans

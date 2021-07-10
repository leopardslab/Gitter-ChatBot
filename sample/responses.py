# Import database configurations and helper functions
import database
import os

# Store some information about the community
about_community = os.getenv('ABOUT_COMMUNITY')
community_website_link = os.getenv('COMMUNITY_WEBSITE')
community_github_link = os.getenv('COMMUNITY_GITHUB')


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
        res = database.collection.find({"tags": q}, {"_id": 0, "tags": 0})
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

# Import the required libraries
import os
import pymongo
from dotenv import load_dotenv
print(__name__)

# Take config variables from the .env file of the project
load_dotenv()
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
CONNECTION_STRING = os.getenv('CONNECTION_STRING')

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

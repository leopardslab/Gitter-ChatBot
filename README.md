# Table of Content
- [Introduction](#introduction)
    - [Dataflow Model](#dataflow-model)
- [Getting Started](#getting-started)
    - [Deployment](#deployment)
- [Contributing](#contributing)
     - [Development Setup](#development-setup)

# Introduction
Gitter-ChatBot exists to guide new contributors with the community projects.

## Dataflow Model
- The Chatbot listens to every chat message in the community's gitter channel with the help of the gitterpy library. An instance of GitterClient with the TOKEN allows a secure connection to the Gitter-API.
The main.py module - It checks the input for three use-case scenarios. The first one is when the existing members are posting to the channel. A second case is when a new contributor comes and asks for help with the community projects. The problem specification of the user can vary from "How to get started?" to "Is this project active?".
- Most queries follow a pattern in which the user prefers to introduce themself then follows their skills/Interests and finally asking the community to recommend them some projects.

![Screenshot from 2021-08-17 13-06-09-1](https://user-images.githubusercontent.com/55585868/129686894-a4630c57-3959-4f2d-b81d-0c0795cbb6ac.png)
![Screenshot from 2021-08-17 13-06-57](https://user-images.githubusercontent.com/55585868/129686897-f3723064-6393-49c1-b905-1a7b4ee8ade3.png)
![Screenshot from 2021-08-17 13-07-34-1](https://user-images.githubusercontent.com/55585868/129686899-4c4496c8-e9b2-4057-abaa-4b8b3775a167.png)

The data_extraction.py module - Gitter-ChatBot has all the possible queries, introduction messages and an expansive list of software technologies stored in JSON data files. It iterates over the user's chat and searches for every word in the data files to understand the user's conversation. The function Keeps a count for every hit, then uses the count to determine the use-case.
A new contributor may or may not provide their skills/interests. In this case, the chatbot explicitly asks the user to do that by giving some commands. Take "@chatbot -p javascript" as an example.
- How to help the people? - The chatbot has its own MongoDB database that stores all the community projects. The data-fields of it are as follows

![image](https://user-images.githubusercontent.com/55585868/129452253-ef51a0a0-dccc-4282-bbe0-9eee06928231.png)

It queries the database to find the projects with the matching skill set, then generates a response to show the list to the user.

# Getting Started
To set up the Gitter-ChatBot for your community locally, you need to follow the following steps:
1. Clone the project, create a virtual environment and install the requirements.txt using pip.
```
git clone https://github.com/leopardslab/Gitter-ChatBot.git
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
2. You need a MongoDB Atlas database to store your community's project.
3. In the example.env file, you need to update all the config variables as described in the file.
4. Rename the `example.env` to `.env` file.
5. Update the database `python src/database.py`. 
**Note** The Github-API only allows 100 repositories per page of the response. In case if you want to add more than 100 projects to the database, update the page parameter in the request url (in the database module `https://api.github.com/orgs/{}/repos?per_page=100&page=1`) to the next page (from 1 to 2 and so on till all the projects get uploaded in the database). Then re-run the step-5 for each page update.
6. Start the Gitter-ChatBot.
```
python src/main.py
```

## Deployment
Follow these instructions to deploy the project on Heroku Cloud using Heroku CLI:
1. Login to your Heroku account. Run `heroku login`.
2. Create a new heroku project. `heroku create`.
3. Open the Heroku web and in your projects's settings, add all the environment variables (.env) to the project's config variables.

![image](https://user-images.githubusercontent.com/55585868/129678787-31926b12-68a0-456d-a8cf-967479ebbeb2.png)
4. Now, push all the src code to the Heroku repository. `git push heroku main`
5. Gitter-ChatBot needs a worker dyno to run continuously and seamlessly. You can turn on the worker dyno either by the CLI command `heroku ps:scale worker=1` or by navigating to the project's resources in the heroku web.

# Contributing
Gitter-ChatBot is always to open to new feature suggestions and bug fixing.

## Development Setup
- To contribute to the Gitter-ChatBot project, you need a fork of the repository.
 
- Cloning the repository
    - Once you have set up your fork of the leopardslab/Gitter-ChatBot repository, you'll want to clone it to your local machine. This is so you can make and test all of your edits before adding it to the master version of leopardslab/Gitter-ChatBot .
    - Navigate to the location on your computer where you want to host your code. Once in the appropriate folder, run the following command to clone the repository to your local machine.
git clone https://github.com/your-username/Gitter-ChatBot.git

### Bootstrapping the repository
 You'll then want to navigate within the folder that was just created that contains all of the content of the forked repository. There you'll want to run the installation script to get the updated version of all the third-party dependencies.
 
 # Gitter-ChatBot Preview
![image](https://user-images.githubusercontent.com/55585868/129679929-c3d4b620-9771-4c04-a561-a8af0feb2bd8.png)

![image](https://user-images.githubusercontent.com/55585868/129680155-0df1749b-8c71-4377-b23a-8ee9aa7f68e8.png)

![image](https://user-images.githubusercontent.com/55585868/129680074-1824bf41-bd67-4aa0-b368-5dd46fe3ea07.png)

![image](https://user-images.githubusercontent.com/55585868/129680464-1c67acfb-3efa-4e6b-852b-681433776c52.png)

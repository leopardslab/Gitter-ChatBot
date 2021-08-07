# Import all the responses to call them based on the extracted information
from . import responses

# Function to process the message and extract the required information given by the user
def process_message(message, username):
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
        'mongodb', 'sql', 'mysql', 'vue.js', 'node.js', 'express.js',
        'blockchain', 'web', 'c++', 'cpp', 'sql', 'mysql', 'golang'
    }

    interests = {
        'machine learning', 'computer vision', 'deep learning',
        'web development', 'android development', 'android', 'mobile',
        'computer vision'
    }

    if message.startswith('@bot -p'):
        count = 3

    for _x_ in introduction:
        if count > 2:
            break
        if _x_ in message:
            count += 1

    if count > 2:
        for _x_ in skills:
            if _x_ in message:
                queries.append(_x_)
        for _x_ in interests:
            if _x_ in message:
                queries.append(_x_)
        if len(queries) != 0:
            return responses.project_suggestion_answer(username, queries)
        return responses.default_suggestion_answer(username)
    return -1

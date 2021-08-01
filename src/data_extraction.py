import json

# load json file
# import 'data.json'

f = open('json_data/search-keywords.json')
data = json.load(f)

# Function to process the message and extract the required information given by the user
def process_message(message):
    # print(message)
    count = 0
    queries = []
    introduction = data['introduction']

    skills = data['skills']

    interests = data['interests']

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
            return queries
            # It returns an array containing all the skills and interests of the user
        return [0]
        # 0 says that the user is a new contributor but has not given any skills or interests
    return [-1]
    # -1 says that the user is not a new contributor and hence do nothing

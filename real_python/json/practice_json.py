import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# it appears you cannot print the responses directly, so you must call
# .txt on it to see it
# >>> response
# <Response [200]>
# >>> response.text
# '[\n  {\n    "userId": 1,\n    "id": 1,\n
todos = json.loads(response.text)
# json.loads loads the text as in json format
# >>> todos
# [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}, {

# Map of userID to number of complete TODOS for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    # "completed": true
    if todo["completed"]:
        try:
            # Increment the existing user's count
            todos_by_user[todo["userId"]] += 1
        # KeyError: Raised when a mapping (dictionary) key is not found in the set of existing keys.
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Created a sorted list of (userId, num_complete)
# lists can be sorted by specific keys
# key = function that takes 1 argument
# the value of a key is often an index position
# lambdas are used to pass a small function as an argument
# below 'lambda x' get ready for the argument
# x = (userId, num_complete)
# x[1] = num_complete
# thus the key for this sorted list is 'completed tasks'
# reverse=True shows in what order to display the key, ex. DESC
# sorted(todos_by_user.items())
# [(1, 11), (2, 8), (3, 7), (4, 6), (5, 12), (6, 6), (7, 9), (8, 11), (9, 8), (10, 12)]
# sorted(todos_by_user.items(), key=lambda x:x[1])
# [(4, 6), (6, 6), (3, 7), (2, 8), (9, 8), (7, 9), (1, 11), (8, 11), (5, 12), (10, 12)]
# sorted(todos_by_user.items(), key=lambda x:x[1],reverse=True)
# [(5, 12), (10, 12), (1, 11), (8, 11), (7, 9), (2, 8), (9, 8), (3, 7), (4, 6), (6, 6)]

top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs
# >>> top_users[0]
# (5, 12)
# The first userId (5) in top_users has a value of 12
# [0] asks for the first user and their number of completed tasks
# [1] applied to the above, only returns an int, the completed tasks
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))
# >>> users
# ['5', '10']

max_users = " and ".join(users)
# >>> max_users
# '5 and 10'

s = "s" if len(users) > 1 else ""
# if s = "s"
# >>> print(f"user{s} {max_users} completed {max_complete} TODOs")
# users 5 and 10 completed 12 TODOs
# if s = ""
# >> print(f"user{s} {max_users} completed {max_complete} TODOs")
# user 5 and 10 completed 12 TODOs

# STILL NEED TO PUT filter todos and write the resulting list
# to a file. For the sake of originality, you can call the
# output file filtered_data_file.json
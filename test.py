import requests
import json
import sql_connector as sql

BASE = "http://localhost:5000/"

data = {
    'email': 'fsaiyad990@gmail.com', 
    'password': 'fs144', 
    'username': 'ReaperFS'
}

response = requests.put(BASE + '/signup', data=data)
print(response)

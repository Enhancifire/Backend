import requests
import json
import sql_connector as sql

BASE = "http://localhost:5000/"

data = {
    'email': 'fsaiyad990@gmail.com', 
    'password': 'fs144'
    
}

response = requests.put(BASE + '/login', data=data)
print(response)

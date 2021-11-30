import requests
import json

BASE = "http://localhost:5000/"

response = requests.get(BASE + '/post/1')
print(response.json())

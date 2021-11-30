import requests
import json

BASE = "http://localhost:5000/"

response = requests.get(BASE + 'signup')
print(response.json())

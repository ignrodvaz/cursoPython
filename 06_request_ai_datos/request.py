import urllib.request
import json
import os
os.system('clear')

# api_posts = "https://jsonplaceholder.typicode.com/posts"

# try:
#     response = urllib.request.urlopen(api_posts)

#     data = response.read()

#     json_data = json.loads(data.decode('utf-8'))

#     print(json_data)

#     response.close()

# except urllib.error.URLError as e:
#     print(f"Error en la solicitud: {e}")

# #Con dependecias requests (GET)
import requests
# print("\nGET:")

# api_posts = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(api_posts)
# json = response.json()
# print(json[0])

#POST
api_posts = "https://jsonplaceholder.typicode.com/posts"
input = {
    "title": "Plataforma streaming con Django",
    "body": "dev",
    "userID": 13
}

response = requests.post(api_posts, json=input)

# print(response.json())
print(response.status_code)
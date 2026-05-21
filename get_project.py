import requests
from requests.auth import HTTPBasicAuth 
import json
import os


url = "https://simplysudipta.atlassian.net/rest/api/3/project/recent"

API_TOKEN = os.getenv("API_TOKEN")
      
auth = HTTPBasicAuth("simplysudipta@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


response = json.loads(response.text)

for project in response:
    print(f"Project Name: {project['name']}")


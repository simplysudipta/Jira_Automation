import requests
from requests.auth import HTTPBasicAuth
import os

url = "https://simplysudipta.atlassian.net/rest/api/3/issue"

API_TOKEN = os.getenv("API_TOKEN")

payload = {
    "fields": {
        "project": {
            "key": "DS"
        },
        "summary": "My first Jira issue",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "type": "text",
                            "text": "Created via API"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Task"
        }
    }
}

response = requests.post(
    url,
    json=payload,
    auth=HTTPBasicAuth("simplysudipta@gmail.com", API_TOKEN),
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
)


print(response.text)
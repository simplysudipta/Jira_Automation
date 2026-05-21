from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import os
import json

app = Flask(__name__)

@app.route('/create_issue', methods=['GET', 'POST'])
def create_issue():
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

    return json.dumps(
        json.loads(response.text),
        sort_keys=True,
        indent=4,
        separators=(",", ": ")
    )

if __name__ == '__main__':
    app.run("0.0.0.0", port=5001)
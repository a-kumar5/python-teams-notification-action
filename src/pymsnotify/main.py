from turtle import color

import requests
import os
from datetime import datetime

datetime_now = datetime.now()
today_date = datetime_now.strftime("%m-%d-%Y")
# get the input
url = os.environ.get("URL")
msg = os.environ.get("MSG")
title = os.environ.get("TITLE")
status = os.environ.get("STATUS")
github_server_url = os.environ.get("GITHUB_SERVER_URL", default="https://github.com")
github_repository = os.environ.get("GITHUB_REPOSITORY")
github_run_id = os.environ.get("GITHUB_RUN_ID")


def main():
    GITHUB_ACTIONS_URL = f"{github_server_url}/{github_repository}/actions/runs/{github_run_id}/"
    content = f"""<a href="{GITHUB_ACTIONS_URL}" target="_blank">[❌] Github Actions | Workflow Failure | Repository: {github_repository} | {today_date}</a>"""
    print(status, type(status))
    send_teams(url, content, title)


def send_teams(webhook_url:str, content:str, title:str, color:str="000000") -> int:
    """
      - Send a teams notification to the desired webhook_url
      - Returns the status code of the HTTP request
        - webhook_url : the url you got from the teams webhook configuration
        - content : your formatted notification content
        - title : the message that'll be displayed as title, and on phone notifications
        - color (optional) : hexadecimal code of the notification's top line color, default corresponds to black
    """
    response = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": color,
            "summary": title,
            "sections": [{
                "activityTitle": title,
                "activitySubtitle": content
            }],
        },
    )
    return response
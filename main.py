import requests
import os

# get the input and convert it to int
url = os.environ.get("URL")
content = os.environ.get("CONTENT")
title = os.environ.get("TITLE")

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
    return response.status_code


#title="Automated Notification about Fruits"
'''content = """
The content of this notification is <i>special</i>.<br>
It is the list of my favorite <b>fruits</b>
<ul>
<li>mango</li>
<li>pineapple</li>
<li>leechi</li>
</ul>
And also a demonstration of an HTML content used for a Teams notification<br>
😍
"""
'''

send_teams(url, content, title)
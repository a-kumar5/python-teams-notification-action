import requests

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


title="Automated Notification about Fruits"
content = """
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

url = "https://searshc.webhook.office.com/webhookb2/34f6d740-a240-4d8e-a030-1b8c5a1ccc03@27e4c168-0323-4463-acad-7e124b566726/IncomingWebhook/3fa80d8d58814d22ad996f9a017737b6/727d96fa-3dd1-4da0-ad93-9b4f153c66fd"
send_teams(url, content, title)
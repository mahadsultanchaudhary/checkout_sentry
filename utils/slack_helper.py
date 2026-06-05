import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_slack_alert(test_name, screenshot_path):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("[Sentry Warning] SLACK_WEBHOOK_URL not configured in environment variables.")
        return

    # Clean up Pytest browser suffixes like test_name[chromium] for clean display
    display_name = test_name.split("[")[0].replace("test_", "").replace("_", " ").title()

    # Highly structured block layout for clarity
    payload = {
        "text": "🚨 Checkout Monitoring Alert",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "🚨 Checkout Monitoring Alert",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Environment:*\nProduction Demo"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Status:*\n`FAILED`"
                    }
                ]
            },
            {
                "type": "section",
                "fields": [
                    {
                        "type": "mrkdwn",
                        "text": f"*Test:*\n{display_name}"
                    },
                    {
                        "type": "mrkdwn",
                        "text": f"*Error Context:*\nExpected confirmation text not found."
                    }
                ]
            },
            
        ]
    }
    
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print(f"[Sentry Error] Slack webhook returned code {response.status_code}: {response.text}")
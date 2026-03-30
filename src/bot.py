import requests
import os
import sys

def send_notification(message):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("Error: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set")
        sys.exit(1)

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print(f"Failed to send notification: {response.text}")
        sys.exit(1)
        
  def format_message(project, branch, date, pr_url, repo_url):
    
    message = (
        f"<b>Pipeline Report</b>\n\n"
        f"<b>Project:</b> {project}\n"
        f"<b>Branch:</b> {branch}\n"
        f"<b>Date:</b> {date}\n\n"
        f"<b>Links</b>\n"
        f"<b>Pull Request:</b> {pr_url}\n"
        f"<b>Repository:</b> {repo_url}\n"
    )
    return message      

    
if __name__ == "__main__":
    test_message = "Test notification from DevOps pipeline"
    send_notification(test_message)

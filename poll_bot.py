import os
import requests

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

data = {
    "chat_id": CHAT_ID,
    "question": "Кто будет в эту субботу на занятии?",
    "options": ["Буду (фолловер)💃", "Буду (лидер)🕺", "Преподаватели👨‍🏫👩‍🏫", "Пропущу🦭"],
    "is_anonymous": False,
    "allows_multiple_answers": False
}

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"
response = requests.post(url, json=data, timeout=30)

print(response.status_code)
print(response.text)
response.raise_for_status()

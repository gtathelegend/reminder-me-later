import requests

url = "http://127.0.0.1:5000/api/reminders/create"
data = {
    "message": "Go for a walk",
    "remind_at": "2025-06-08T18:00:00",
    "method": "email"
}

response = requests.post(url, json=data)
print(response.json())

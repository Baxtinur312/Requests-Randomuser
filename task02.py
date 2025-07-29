import requests
import json

# API dan 10 ta foydalanuvchi olish
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()

# Foydalanuvchilar ro'yxatini tayyorlash
users = []
for user in data['results']:
    user_info = {
        "full_name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "gender": user['gender'],
        "country": user['location']['country']
    }
    users.append(user_info)

# users.json faylga saqlash
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, indent=2, ensure_ascii=False)

print(f"{len(users)} ta foydalanuvchi users.json faylga saqlandi!")
for i, user in enumerate(users, 1):
    print(f"{i}. {user['full_name']} - {user['country']}")
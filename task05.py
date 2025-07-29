import requests
import json
from datetime import datetime

# API dan 20 ta foydalanuvchi olish
url = "https://randomuser.me/api/?results=20"
response = requests.get(url)
data = response.json()

# 1990-yildan keyin tug'ilganlarni ajratish
young_users = []
for user in data['results']:
    # Tug'ilgan sanani parse qilish
    birth_date = user['dob']['date']
    birth_year = int(birth_date[:4])  # "1998-05-17T10:23:45.123Z" dan 1998 ni olish
    
    # Faqat 1990-yildan keyin tug'ilganlarni qo'shish
    if birth_year > 1990:
        user_info = {
            "name": f"{user['name']['first']} {user['name']['last']}",
            "birth_year": birth_year,
            "email": user['email']
        }
        young_users.append(user_info)

# young_users.json faylga saqlash
with open('young_users.json', 'w', encoding='utf-8') as f:
    json.dump(young_users, f, indent=2, ensure_ascii=False)

print(f"{len(young_users)} ta yosh foydalanuvchi (1990-yildan keyin tug'ilgan) saqlandi!")
for i, user in enumerate(young_users, 1):
    print(f"{i}. {user['name']} - {user['birth_year']}")
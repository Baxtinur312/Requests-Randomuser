import requests
import json

# API dan 10 ta ayol foydalanuvchi olish
url = "https://randomuser.me/api/?results=10&gender=female"
response = requests.get(url)
data = response.json()

# Ayol foydalanuvchilar ro'yxatini tayyorlash
females = []
for user in data['results']:
    user_info = {
        "name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "phone": user['phone'],
        "country": user['location']['country']
    }
    females.append(user_info)

# females.json faylga saqlash
with open('females.json', 'w', encoding='utf-8') as f:
    json.dump(females, f, indent=2, ensure_ascii=False)

print(f"{len(females)} ta ayol foydalanuvchi females.json faylga saqlandi!")
for i, user in enumerate(females, 1):
    print(f"{i}. {user['name']} - {user['country']}")
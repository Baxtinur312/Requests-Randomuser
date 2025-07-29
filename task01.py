import requests
import json

# API dan bitta foydalanuvchi olish
url = "https://randomuser.me/api/"
response = requests.get(url)
data = response.json()

# Foydalanuvchi ma'lumotlarini ajratish
user = data['results'][0]
user_info = {
    "first_name": user['name']['first'],
    "last_name": user['name']['last'],
    "gender": user['gender'],
    "email": user['email'],
    "phone": user['phone'],
    "address": {
        "street": user['location']['street']['name'],
        "city": user['location']['city'],
        "country": user['location']['country']
    }
}

# user.json faylga saqlash
with open('user.json', 'w', encoding='utf-8') as f:
    json.dump(user_info, f, indent=2, ensure_ascii=False)

print("Bitta foydalanuvchi user.json faylga saqlandi!")
print(json.dumps(user_info, indent=2, ensure_ascii=False))
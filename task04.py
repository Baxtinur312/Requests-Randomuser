import requests
import json

# API dan 10 ta foydalanuvchi olish
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()

# Foydalanuvchilarni rasm URL bilan tayyorlash
users_with_images = []
for user in data['results']:
    user_info = {
        "name": f"{user['name']['first']} {user['name']['last']}",
        "email": user['email'],
        "image_url": user['picture']['large']
    }
    users_with_images.append(user_info)

# users_with_images.json faylga saqlash
with open('users_with_images.json', 'w', encoding='utf-8') as f:
    json.dump(users_with_images, f, indent=2, ensure_ascii=False)

print(f"{len(users_with_images)} ta foydalanuvchi rasm URL bilan saqlandi!")
for i, user in enumerate(users_with_images, 1):
    print(f"{i}. {user['name']} - {user['image_url']}")
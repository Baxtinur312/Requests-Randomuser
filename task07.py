import requests
import os

# images papkasini yaratish
if not os.path.exists('images'):
    os.makedirs('images')

# API dan 5 ta foydalanuvchi olish
url = "https://randomuser.me/api/?results=5"
response = requests.get(url)
data = response.json()

print("Rasmlarni yuklab olish boshlandi...")

# Har bir foydalanuvchining rasmini yuklab olish
for i, user in enumerate(data['results'], 1):
    try:
        # Rasm URL'ini olish
        image_url = user['picture']['large']
        
        # Rasmni yuklab olish
        img_response = requests.get(image_url)
        img_response.raise_for_status()  # HTTP xatolikni tekshirish
        
        # Rasmni faylga saqlash
        filename = f"images/user{i}.jpg"
        with open(filename, 'wb') as f:
            f.write(img_response.content)
        
        user_name = f"{user['name']['first']} {user['name']['last']}"
        print(f"{i}. {user_name} rasmi saqlandi: {filename}")
        
    except requests.exceptions.RequestException as e:
        print(f"{i}-foydalanuvchi rasmini yuklab olishda xatolik: {e}")
    except Exception as e:
        print(f"Umumiy xatolik {i}-foydalanuvchi uchun: {e}")

print(f"\nJami {len(data['results'])} ta foydalanuvchi rasmi images/ papkasiga saqlandi!")
import requests
import csv

# API dan 10 ta foydalanuvchi olish
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
data = response.json()

# CSV fayl yaratish
with open('users.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Full Name', 'Gender', 'Email', 'Phone', 'Country']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Header yozish
    writer.writeheader()
    
    # Har bir foydalanuvchi ma'lumotlarini yozish
    for user in data['results']:
        writer.writerow({
            'Full Name': f"{user['name']['first']} {user['name']['last']}",
            'Gender': user['gender'],
            'Email': user['email'],
            'Phone': user['phone'],
            'Country': user['location']['country']
        })

print("Foydalanuvchilar users.csv faylga saqlandi!")

# CSV faylni o'qib, natijani ko'rsatish
print("\nCSV fayl mazmuni:")
with open('users.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            print("Header:", ", ".join(row))
        else:
            print(f"User {i}: {', '.join(row)}")
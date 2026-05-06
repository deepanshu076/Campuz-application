import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campuz.settings')
django.setup()

from django.test import Client

client = Client()
response = client.post('/signup/', {
    'username': 'testuser',
    'email': 'test@test.com',
    'password': 'password123',
    'confirm_password': 'password123',
    'role': 'student'
})

print(f"Status Code: {response.status_code}")
if response.status_code in (301, 302):
    print(f"Redirected to: {response.url}")

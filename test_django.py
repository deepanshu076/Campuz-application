from django.test import Client
c = Client()
response = c.post('/signup/', {'username': 'test', 'email': 'test@test.com', 'password': 'password123', 'confirm_password': 'password123'})
print("STATUS:", response.status_code)

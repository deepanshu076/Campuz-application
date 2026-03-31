import traceback
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'campuz.settings')
django.setup()

from users.models import User

try:
    User.objects.create_user('hod_cs_3', 'hod3@campuz.com', 'pwd_hod', role='hod', department='Computer Science')
    print("Success")
except Exception as e:
    traceback.print_exc()

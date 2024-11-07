
import os
import django
from faker import Faker
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'userproject.settings')
django.setup()
 
from user_app.models import User
 
def populate(5):
    fake = Faker()
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        User.objects.create(first_name=first_name, last_name=last_name, email=email)
        

if __name__ == '__main__':
    print("Populating the database...please wait.")
    populate(15)
    print("Populating complete.")
 


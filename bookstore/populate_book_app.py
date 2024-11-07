import os
import django
from faker import Faker
from random import *
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()
 
from book_app.models import BookInfo

def populate(n):
    fake = Faker()
    for i in range(n):
        title = fake.title()
        author = fake.author()
        description = fake.description()
        price = fake.price()
        publication_date = fake.publication_date()
        BookInfo.objects.create(title=title,author=author,description=description,price=price,publication_date = publication_date)
        
populate(10)
if __name__ == '__main__':
   print("Populating the database...please wait.")
   populate(15)
   print("Populating complete.")
 
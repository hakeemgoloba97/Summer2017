import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','summerProject.settings')

import django
# Import settings
django.setup()
import string

import random
from faker import Faker
from mainApp.models import userInfo
from django.contrib.auth.models import User

import csv


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    fake = Faker()

    print(N)
    for i in range(N):
        name = fake.name().split(" ")
        user = User.objects.get_or_create(
                                              username = name[0]+name[1],
                                              email= fake.email(),
                                              password= ''.join([random.choice(string.ascii_letters + string.digits) for n in range(8)]))[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(942)
    print('Populating Complete')

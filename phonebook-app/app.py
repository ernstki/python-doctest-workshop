import random

from flask import Flask, render_template
from faker import Faker
from faker.providers import phone_number

fake = Faker()
fake.add_provider(phone_number)

people = []
app = Flask(__name__)

for i in range(0, random.randint(20,50)):
    people.append([fake.last_name(), fake.first_name(), fake.phone_number()])

# import pdb; pdb.set_trace()

@app.route('/')
def index():
    return render_template('index.html', people=people)







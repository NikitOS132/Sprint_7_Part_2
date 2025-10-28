from faker import Faker
import random

fake = Faker()

def login_generator():
    generated_login = fake.user_name()
    return generated_login

def password_generator():
    generated_password = fake.random_number(5)
    return generated_password

def name_generator():
    generate_name = fake.first_name()
    return generate_name

def false_login_generator():
    false_login = fake.user_name()
    return false_login

def false_password_generator():
    false_password = fake.random_number(5)
    return false_password

def first_name_generator():
    first_name = fake.first_name_male()
    return first_name

def last_name_generator():
    last_name = fake.last_name_male()
    return last_name

def address_generator():
    address = fake.street_address()
    return address

def phone_generator():
    phone = fake.phone_number()
    return phone

def rent_time_generator():
    rent_time = random.randint(1, 3)
    return rent_time

def delivery_date_generator():
    delivery_date = fake.date()
    return delivery_date

def metro_generator():
    metro = random.randint(1, 2)
    return metro

def comment_generator():
    comment = fake.word()
    return comment
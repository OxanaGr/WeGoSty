from faker import Faker
fake = Faker(locale='en_CA')

app = 'WeGoStudy'
wegosty_url = 'http://34.233.225.85/students/admissions'
wegosty_homepage_url = 'http://34.233.225.85/'
werosty_home_page_title = ''
first_name = fake.first_name()
last_name = fake.last_name()
passport_number = f'Pa{fake.pyint(11, 9999)}'
phone_number = fake.phone_number()
mailing_address = fake.street_address()
user_email = fake.email()
postal_code = fake.postalcode()
date_of_birth = fake.date_of_birth(minimum_age = 16)



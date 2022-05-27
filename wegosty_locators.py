from faker import Faker
fake = Faker(locale='en_CA')

app = 'WeGoStudy'
partner_name = 'xxxxx'
partner_pass = 'xxxxxxx!'
# wegosty_url = 'http://34.233.225.85/students/admissions'
wegosty_url = 'https://wegostudy.ca/partner/home'
wegosty_homepage_url = 'http://34.233.225.85/'
werosty_home_page_title = ''
first_name = fake.first_name()
last_name = fake.last_name()
passport_number = f'PA{fake.random_int(100000, 999999)}'
phone_number = fake.phone_number()
# apartment_number =
mailing_address = fake.street_address()
user_email = fake.email()
college_ID = fake.random_int(10000, 99999)
student_permit_number = f'SP{fake.random_int(10000, 99999)}'
first_language = 'English'
# school = 'Douglas College'

# province_state =
# city =
postal_code = fake.postalcode()
# user_email =
# school_name =
# program =
# gpa =
date_of_birth = fake.date_of_birth(minimum_age = 16)



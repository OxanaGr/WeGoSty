from faker import Faker
fake = Faker(locale='en_CA')

app = 'WeGoStudy'
wegosty_url = 'http://34.233.225.85/students/admissions'
werosty_home_page_title = ''
first_name = fake.first_name()
last_name = fake.last_name()
passport_number = fake.pyint(1111111, 9999999)
phone_number = fake.phone_number()
# apartment_number =
mailing_address = fake.street_address()
user_email = fake.email()
# province_state =
# city =
postal_code = fake.postalcode()
# user_email =
# school_name =
# program =
# gpa =

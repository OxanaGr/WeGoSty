from selenium import webdriver
import wegosty_locators as locators
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
import sys
import random

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'lanch {locators.app}')
    print('___________________________________________')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get('http://34.233.225.85/students/admissions')
    if driver.current_url == 'http://34.233.225.85':
        print(f' WeGoStudy URL: {driver.current_url}')

def login():
    driver.find_element(By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[1]').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'LOGIN').click()
    sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys('chris.velasco78@gmail.com')
    sleep(1)
    driver.find_element(By.ID, 'user_password').send_keys('123cctb')
    sleep(1)
    driver.find_element(By.XPATH, "//input[@value='SIGN IN']").click()
    # driver.find_element(By.NAME, 'commit').click()
    # driver.find_element(By.XPATH,'//*[@id="new_user"]/div[3]/input').click()


def log_out():
    sleep(8)
    driver.find_element(By.XPATH,'//div[@id="navbar-nav"]/ul[2]/li[2]/a/span').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Log out').click()

def create_new_student():
    driver.find_element(By.LINK_TEXT, 'My WeGoStudy').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Create New Student').click()
    sleep(1)
    # __________________Personal_Information______________________________
    driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_preferred_name').send_keys(locators.first_name)
    sleep(0.3)
    driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
    sleep(0.3)
    driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//input[@type="search"]' ).send_keys('Canada')
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_country_of_citizenship"]/option[40]').click()
    sleep(0.3)
    driver.find_element(By.ID,'user_student_detail_attributes_passport_number').send_keys(locators.passport_number)
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('2000-03-15')
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('2000 03 1')
    sleep(0.3)
    # __________________Contact Information______________________________
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.mailing_address)
    sleep(0.3)
    driver.find_element(By.LINK_TEXT, 'Country').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/ul/li[40]').click()
    sleep(0.6)
    driver.find_element(By.LINK_TEXT, 'Province/State').click()
    sleep(0.6)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/ul/li[3]').click()
    sleep(0.6)
    driver.find_element(By.LINK_TEXT, 'City').click()
    sleep(0.6)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li[30]').click()
    sleep(0.6)
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(locators.postal_code)
    sleep(0.6)
    driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
    sleep(0.6)
    # __________________Education Information______________________________
    driver.find_element(By.LINK_TEXT, 'Credentials').click()
    sleep(0.6)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/ul/li[3]').click()
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_school_name').send_keys('CCTB')
    sleep(0.3)
    driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_program').send_keys('SQTA')
    sleep(0.3)
    driver.find_element(By.XPATH, '//div[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/a/span').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//div[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/ul/li[5]').click()
    sleep(0.3)
    # __________________________________________
    driver.find_element(By.ID, 'user_student_detail_attributes_user_educations_attributes_0_gpa').send_keys('4.0')
    sleep(0.3)
    driver.find_element(By.XPATH, '//input[@value="Save"]').click()




def tearDown():
    if driver is not None:
        print(f'_________________Test finished successfully at {datetime.datetime.now()}_________________')
        sleep(2)
        driver.close()
        driver.quit()

        


setUp()
login()
# create_application()
create_new_student()
# search_student()
# delete_studnt()
log_out()
# tearDown()

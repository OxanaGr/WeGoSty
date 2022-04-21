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
    driver.find_element(By.ID,'navbar-nav').click()
    driver.find_element(By.XPATH, '//*[@id="navbar-nav"]/ul[2]/li[2]/div/a[4]').click()


def create_application():
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbar-nav"]/ul[1]/li[1]/a/span').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="navbar-nav"]/ul[1]/li[1]/div/a[3]').click()
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/section/div/div/div/div/div/a').click()
    sleep(1)


def tearDown():
    if driver is not None:
        print(f'_________________Test finished successfully at {datetime.datetime.now()}_________________')
        sleep(2)
        driver.close()
        driver.quit()

        logger('delleted')

def logger(action: object):
    old_instance = sys.stdout
    log_file = open('message.log', 'a')
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.username}\t'
          f'{locators.password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()

setUp()
login()
# create_application()
# creat_student()
# search_student()
# delit_studnt()
# log_out()
# tearDown()
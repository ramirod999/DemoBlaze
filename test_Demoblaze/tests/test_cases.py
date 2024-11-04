import time
from pages.elements import AllElements as Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import driver
import pytest
from selenium.common.exceptions import ElementNotInteractableException

def test_case_one(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    apple_mon_selector = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
    asus_mon_selector = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    lo = Locators(driver)
    lo.click_monitors()
    time.sleep(5)

    # Wait for the elements to be present
    apple_mon_element = wait.until(EC.presence_of_element_located(apple_mon_selector))
    asus_mon_element = wait.until(EC.presence_of_element_located(asus_mon_selector))
    time.sleep(3)

    # Use the correct method to check if elements are displayed
    assert apple_mon_element.is_displayed() and asus_mon_element.is_displayed()
    time.sleep(3)

def test_case_two(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    macbook_air = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    el = Locators(driver)
    el.click_monitors()
    time.sleep(2)
    el.click_next()
    time.sleep(3)
    macbook_air_element = wait.until(EC.presence_of_element_located(macbook_air))
    assert macbook_air_element.is_displayed()

def test_case_three(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    nokia_lumia = (By.XPATH   ,'/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    lo= Locators(driver)
    lo.click_monitors()
    time.sleep(3)
    lo.click_next()
    time.sleep(3)
    lo.click_prev()
    time.sleep(3)
    nokia_lumia_element = wait.until(EC.presence_of_element_located(nokia_lumia))
    assert nokia_lumia_element.is_displayed()

def test_case_four(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    nexus=(By.XPATH ,'/html/body/nav/div[2]/div/div/div[2]/img')

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    time.sleep(3)
    lo = Locators(driver)
    lo.next_arrow_btn()
    time.sleep(3)
    nexus_element = wait.until(EC.presence_of_element_located(nexus))
    assert nexus_element.is_displayed()

def test_case_five(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    nexus_pic=(By.CSS_SELECTOR,'#imgp > div > img')

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    time.sleep(3)
    el = Locators(driver)
    el.click_phones()
    time.sleep(3)
    el.click_nokia()
    time.sleep(3)
    nexus_element = wait.until(EC.presence_of_element_located(nexus_pic))
    assert nexus_element.is_displayed()


@pytest.mark.parametrize('user_name, pass_word',[
    ('rami', '123'),
    ('random1', 'random2'),
    ('123', '123')
])
def test_case_six(driver,user_name,pass_word):
    base_url = 'https://www.demoblaze.com/index.html'
    welcome_123=(By.XPATH,'/html/body/nav/div[1]/ul/li[7]/a')
    username_field = (By.XPATH,'/html/body/div[3]/div/div/div[2]/form/div[1]/input')
    password_field =(By.ID, "loginpassword")
    login_btn = (By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')

    wait = WebDriverWait(driver, 10)
    username= user_name
    password= pass_word

    driver.get(base_url)
    time.sleep(3)
    el = Locators(driver)
    el.click_login_btn()
    time.sleep(5)
    username_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(username_field))
    username_element.send_keys(username)
    # el.username_field_element()
    time.sleep(3)
    password_element = wait.until(EC.presence_of_element_located(password_field))
    password_element.send_keys(password)
    # el.enter_password()
    time.sleep(5)
    login_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(login_btn))
    login_element.click()
    time.sleep(5)

    # el.click_login_btn()
    welcome_element = wait.until(EC.presence_of_element_located(welcome_123))
    assert welcome_element.is_displayed()

def test_case_seven(driver):
    base_url = 'https://www.demoblaze.com/index.html'

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    time.sleep(3)
    lo = Locators(driver)
    time.sleep(3)
    lo.click_categories_btn()
    time.sleep(3)
    current_url='https://www.demoblaze.com/index.html'
    assert current_url == driver.current_url

def test_case_eight(driver):
    base_url = 'https://www.demoblaze.com/index.html'

    wait = WebDriverWait(driver, 10)
    driver.get(base_url)
    time.sleep(3)
    lo = Locators(driver)
    lo.click_contact_btn()
    time.sleep(3)
    lo.click_close_btn()

@pytest.mark.parametrize('contact_name, contact_email,contact_msg',[
    ('pablo', 'testemail@gmail.com','you have a really terrible website its crazy'),
    ('random1', 'random2','random3'),
    ('1','12','horrible website '),
    ('pablo','@gmail.com','-'),
    ('pneumonoultramicroscopicsilicovolcanoconiosis','testemail@gmail.com','hello i really like your website'),
    ('','','')
])
def test_case_nine(driver,contact_name,contact_email,contact_msg):
    base_url = 'https://www.demoblaze.com/index.html'
    email_fieldi = (By.ID,'recipient-email')
    name_fieldi =(By.ID, 'recipient-name')
    msg_fieldi = (By.ID ,'message-text')

    wait = WebDriverWait(driver, 10)
    emailfield = contact_email
    namefield = contact_name
    msgfield = contact_msg

    driver.get(base_url)

    lo = Locators(driver)
    lo.click_contact_btn()
    time.sleep(12)

    emailfield_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(email_fieldi))
    emailfield_element.send_keys(emailfield)


    namefield_element = wait.until(EC.presence_of_element_located(name_fieldi))
    namefield_element.send_keys(namefield)

    msgfield_element = wait.until(EC.presence_of_element_located(msg_fieldi))
    msgfield_element.send_keys(msgfield)

    lo.click_send_msg_contact()
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Alert message: {alert_text}")
    alert.accept()

# def test_case_ten(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#
#     wait = WebDriverWait(driver, 10)
#     driver.get(base_url)
#     lo = Locators(driver)
#     # time.sleep(10)
#     for i in range(25):
#         time.sleep(1)
#
#         lo.click_next()
#         # time.sleep(1)
#
#         lo.click_prev()
#         # time.sleep(1)

def test_case_ten(driver):
    base_url = 'https://www.demoblaze.com/index.html'

    # Initialize the browser (assuming you're using Chrome)
    lo =Locators(driver)

    try:
        # Navigate to the Demoblaze website
        driver.get(base_url)
        lo = Locators(driver)

        # Loop through 25 iterations (Next + Prev)
        for i in range(25):
            time.sleep(1)

            try:
                lo.click_next()
                # time.sleep(1)
            except ElementNotInteractableException:
                print("ElementNotInteractableException occurred while clicking 'Next'.")
            try:
                lo.click_prev()
                # time.sleep(1)
            except ElementNotInteractableException:
                print("ElementNotInteractableException occurred while clicking 'Prev'.")

            assert base_url == driver.current_url

    finally:
        driver.quit()





















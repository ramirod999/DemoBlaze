from tests.conftest import driver
from .base_page_autoprac import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AllElements(BasePage):
    """Class to represent the login page actions"""
    username_field = (By.XPATH,'/html/body/div[3]/div/div/div[2]/form/div[1]/input')
    password_field =(By.ID, "loginpassword")
    LOGIN_BUTTON = (By.ID,"login2")
    monitors_tab = (By.XPATH  ,'/html/body/div[5]/div/div[1]/div/a[4]')
    next_btn = ( By.ID ,'next2')
    prev_btn = (By.ID ,'prev2')
    apple_mon = (By.XPATH ,'/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
    asus_mon = (By.XPATH  ,'/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')
    macbook_air=(By.XPATH   ,'/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')
    arrow_btn=(By.CSS_SELECTOR ,'#carouselExampleIndicators > a.carousel-control-next > span.carousel-control-next-icon')
    phones_btn=(By.XPATH    ,'/html/body/div[5]/div/div[1]/div/a[2]')
    nokia_lumia_btn=(By.XPATH   ,'/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')
    click_login = (By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')
    categories_btn=(By.ID,'cat')
    close_btn=(By.XPATH,'/html/body/div[1]/div/div/div[3]/button[1]')
    contact_us_btn=(By.XPATH,'/html/body/nav/div[1]/ul/li[2]/a')
    send_msg_btn=(By.XPATH,'/html/body/div[1]/div/div/div[3]/button[2]')


    def apple_mon_element(self, apple_mon):
        return self.find_element(apple_mon)

    def asus_mon_element(self, asus_mon):
        return self.find_element(asus_mon)

    def macbook_air_element(self, macbook_air):
        return self.find_element(macbook_air)

    def click_monitors(self):
        self.click_element(self.monitors_tab)

    def click_login_btn(self):
        self.click_element(self.click_login)

    def click_contact_btn(self):
        self.click_element(self.contact_us_btn)

    def click_send_msg_contact(self):
        self.click_element(self.send_msg_btn)

    def click_categories_btn(self):
        self.click_element(self.categories_btn)

    def click_close_btn(self):
        self.click_element(self.close_btn)

    def click_phones(self):
        self.click_element(self.phones_btn)

    def click_nokia(self):
        self.click_element(self.nokia_lumia_btn)

    def click_next(self):
        self.click_element(self.next_btn)

    def next_arrow_btn(self):
        self.click_element(self.arrow_btn)

    def click_prev(self):
        self.click_element(self.prev_btn)

    def enter_username(self,username):
        self.enter_text(self.username_field,username)

    def enter_password(self,password):
        self.enter_text(self.passworld_field,password)
        """enters password in password field"""

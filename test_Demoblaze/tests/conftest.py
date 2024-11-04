import os
import pytest
from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Set webdriver manager  to use the local  cache
os.environ['WDM_LOCAL'] = '1'


@pytest.fixture(scope="session")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_services = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_services, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
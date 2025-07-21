from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver_path = '/path/to/chromedriver'
driver = webdriver.Chrome(chromedriver_path)
login_url = 'https://example.com/login'
driver.get(login_url)
username_field = driver.find_element_by_id('username')
password_field = driver.find_element_by_id('password')
username = 'your_username'
password = 'your_password'

username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

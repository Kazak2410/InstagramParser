from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os


load_dotenv()

with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.instagram.com/")
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.send_keys(os.getenv('LOGIN'))

    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(os.getenv('PASSWORD'))

    password_input.send_keys(Keys.RETURN)
    time.sleep(10)

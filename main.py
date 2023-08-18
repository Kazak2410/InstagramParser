import os
import time
import csv
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


load_dotenv()


def check_notification(wait):
    try:
        notification_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "._a9--._a9_1")))
        notification_input.click()
    except TimeoutException:
        print("Notification element not found within the specified time.")


def find_users(driver, keyword):
    search_button_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a"
    search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_button_xpath)))
    search_button.click()
    time.sleep(5)

    search_input_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input"
    search_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_input_xpath)))
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.RETURN)
    time.sleep(5)

    users_xpath = "x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"
    users = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, f'//*[@class="{users_xpath}"]')))

    return users


with webdriver.Chrome() as driver:
    with open("data.csv", "w") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    ["user_account"]
                )

    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.instagram.com/")
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.send_keys(os.getenv("LOGIN"))

    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(os.getenv("PASSWORD"))
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    check_notification(wait)

    keyword = input("Enter the keyword:")

    users = find_users(driver, keyword)

    users_to_proccess = list(users)

    for user_index in range(len(users)):
        user = users[user_index]
        user_url = user.get_attribute("href")
        print(user_url)
        user.click()
        time.sleep(random.randrange(5, 15))
        try:
            user_status = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='_aa_u']")))
            print("Account is closed")
            users = find_users(driver, keyword)
        except:
            try:
                subscribe_button_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button"
                subscribe_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, subscribe_button_xpath)))
                subscribe_button.click()
                time.sleep(random.randrange(80, 100))

                send_message_button_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div"
                send_message_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, send_message_button_xpath)))
                send_message_button.click()
                time.sleep(random.randrange(10, 50))

                check_notification(wait)

                send_message_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]"
                send_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, send_message_xpath)))
                send_message.send_keys('Hi')
                send_message.send_keys(Keys.RETURN)

                with open("data.csv", "a", newline="") as file:
                    writer = csv.writer(file, delimiter=';')

                    writer.writerow(
                        [user_url]
                    )
                print("User has been added")

                users = find_users(driver, keyword)
            except:
                 print('The message could not be sent')
                 users = find_users(driver, keyword)

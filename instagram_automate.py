#https://realpython.com/instagram-bot-python-instapy/
#pip install selenium
#install firefox browser
# install firefox gecko driver -https://github.com/mozilla/geckodriver/releases - geckodriver-v0.31.0-macos.tar.gz
#add gecko to PATH https://www.kenst.com/including-the-chromedriver-location-in-macos-system-path/

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login_link = browser.find_element(By.ID,'loginForm')
login_link.click()

sleep(2)

username_input = browser.find_element(By.NAME,'username')
password_input = browser.find_element(By.NAME,'password')

username_input.send_keys("xxx")
password_input.send_keys("xxx")


login_button = browser.find_element(By.XPATH,"//button[@type='submit']")
login_button.click()

sleep(5)

browser.close()

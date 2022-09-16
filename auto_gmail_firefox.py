#https://stackoverflow.com/questions/66209119/automation-google-login-with-python-and-selenium-shows-this-browser-or-app-may
#https://www.geeksforgeeks.org/gmail-login-using-python-selenium/
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

geckodriver_autoinstaller.install()

profile = webdriver.FirefoxProfile(
    '/Users/anup/Library/Application Support/Firefox/Profiles/8p9uia4x.default-release')

profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX

driver = webdriver.Firefox(firefox_profile=profile,
                           desired_capabilities=desired)

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.gmail.com/')

sleep(5)

loginBox = browser.find_element(By.XPATH,'//*[@id ="identifierId"]')
loginBox.send_keys("anueinstein@gmail.com")

sleep(2)

nextButton = browser.find_element(By.XPATH,'//*[@id ="identifierNext"]')
nextButton.click()

sleep(2)

passWordBox = browser.find_element(By.XPATH,
    '//*[@type ="password"]')


sleep(5)

passWordBox.send_keys("pappupattu")



nextButton = browser.find_element(By.XPATH,'//*[@id ="passwordNext"]')
nextButton[0].click()

sleep(5)

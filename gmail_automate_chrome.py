#pip install selenium
#install firefox browser
# install firefox gecko driver -https://github.com/mozilla/geckodriver/releases - geckodriver-v0.31.0-macos.tar.gz
#add gecko to PATH https://www.kenst.com/including-the-chromedriver-location-in-macos-system-path/
#https://www.geeksforgeeks.org/gmail-login-using-python-selenium/
#pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

print('Enter the gmailid and password')
gmailId, passWord = map(str, input().split())
print("gmailId - ",gmailId, "passWord- ",passWord )
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
	'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
	'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
	driver.implicitly_wait(15)

	loginBox = driver.find_element(By.XPATH,'//*[@id ="identifierId"]')
	loginBox.send_keys(gmailId)

	print("sending gmail user name:")

	nextButton = driver.find_element(By.XPATH,'//*[@id ="identifierNext"]')
	nextButton.click()

	print("clicked the next button successfully")



	passWordBox = driver.find_element(By.XPATH,
		'//*[@type ="password"]')
	print("found password box using css type", passWordBox)

	sleep(15)

	passWordBox.send_keys(passWord)

	print("sent password successfully")

	nextButton = driver.find_element(By.XPATH,'//*[@id ="passwordNext"]')
	nextButton[0].click()

	print("clciked next after sending password")

	print('Login Successful...!!')
except Exception as inst:
	print(type(inst))    # the exception instance
	print(inst.args)     # arguments stored in .args
	print(inst)          # __str__ allows args to be printed directly,
	                           # but may be overridden in exception subclasses
	x, y = inst.args     # unpack args
	print('x =', x)
	print('y =', y)

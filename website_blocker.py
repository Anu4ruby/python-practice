#https://www.geeksforgeeks.org/website-blocker-using-python/
#vi /etc/hosts - has a list of local hosts with ip address
# Run this script as root
#sudo crontab -e
# add the below line into crontab
#@reboot python3 Users/anup/python-workspace/python-practice/website_blocker.py


import time
from datetime import datetime as dt

# change hosts path according to your OS
hosts_path = "/etc/hosts"
# localhost's IP
localhost_ip = "127.0.0.1"

# websites That you want to block
website_list = ["www.facebook.com","facebook.com",
	"twitter.com","www.twitter.com"]

while True:

	# time of your work 9AM- 5PM
	if dt(dt.now().year, dt.now().month, dt.now().day,9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,17):
		print("Working hours...")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					# mapping hostnames of websites to be blocked to your localhost IP address
					file.write(localhost_ip + " " + website + "\n")
	else:
		with open(hosts_path, 'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)

			# removing hostnmes from host file
			file.truncate()

		print("unblock the website after work hours...")
	time.sleep(5)

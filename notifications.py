#Desktop notifications
# pip install requests
# pip install pyobjus
#https://www.javatpoint.com/desktop-notifier-in-python

from plyer import notification
import time

notification_title = 'GREETINGS!'
notification_message = 'Have a Good Day.'

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 10,
    toast = False
    )
time.sleep(10)

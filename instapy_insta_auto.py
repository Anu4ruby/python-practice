#https://realpython.com/instagram-bot-python-instapy/
#python3 -m pip install instapy
from instapy import InstaPy
session = InstaPy(username="xxx", password="xxx",headless_browser=False,want_check_browser=False)
session.login()

'''
session.like_by_tags(["bmw", "mercedes"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
'''
session.end()

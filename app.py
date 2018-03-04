from selenium import webdriver

from getpass import getpass
import json
import facebook
import urllib
import requests
from urllib.parse import urlparse

driver = webdriver.Firefox(executable_path=r'C:\Users\joyce\Desktop\bachelor\geckodriver-v0.19.1-win64\geckodriver.exe')

my_access_token = 'EAAXqKhlDlkcBAMrwVR68a9zK4aALfvw26CmVrShjtkCevKCHZAhD8KbupZBQkkYBqswHuo14z6rrHhfVjNEoEeR'
FACEBOOK_APP_ID= '1664841416939079'
FACEBOOK_APP_SECRET = '70e0a8b22eccbab11ee6f3a8306152bd'

#chosing code not accesstoken irectly cause accesstoken is hashed  Client-side JavaScript can capture URL fragments (for example jQuery BBQ),
#  whereas URL parameters can be captured by both client-side and server-side code accesstoken is a fragment while code is a parameter
r = driver.get('https://www.facebook.com/v2.12/dialog/oauth?client_id={}&redirect_uri={}&response_type={}&scope={}'.format(FACEBOOK_APP_ID,'http://localhost:8080/','code','email,publish_actions,user_about_me'))






#trials

# from facebookads.api import FacebookAdsApi
# from facebookads import objects



# usr=input('enter your email : ')
# pwd=getpass('enter your pass: ')

# driver.get('https://www.facebook.com/')
# user=driver.find_element_by_id('email')
# user.send_keys(usr)
#
# user=driver.find_element_by_id('pass')
# user.send_keys(pwd)
#
# login=driver.find_element_by_id('u_0_3')
# login.submit()
# facebook.FACEBOOK_OAUTH_DIALOG_URL
# fb=facebook.init(my_app_id, my_app_secret, my_access_token)

# r=requests.get('https://www.facebook.com/user', auth=(usr, pwd))
# print(r.text)


#requests.Session().getCurrentAccessToken()
#driver.get('https://www.facebook.com/v2.12/dialog/oauth?client_id={1664841416939079}&redirect_uri={https://www.facebook.com}&state={l}&scope={{ FACEBOOK_EXTENDED_PERMISSIONS }}')


#r = requests.get('https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=usr&client_secret=pwd')
#access_token = r.text.split('=')[1]
#driver.get(https://graph.facebook.com/oauth/access_token?grant_type=client_credentials&client_id=usr&client_secret=pwd)
#print(r.status_code)
#r = requests.get('https://www.facebook.com/dialog/oauth', auth=(usr, pwd))

# token='EAAXqKhlDlkcBADWju70UyIFLxSAZBjFtB7vh1ED8op3wR8RKpUbrud8vsFho6ieoxpINIlYnGcCiZBHmqjryOrgGLkpOnrYh3wZB1Q7CkzA0kUg09xaB4p1C1AsZB1XdYhJc8fkpmznJYHkZAQRZAVn9920TAhMqTztJQg2vaiIA9wL5Jr4qVepDD4iais3hH6xZAmYmV6MQQZDZD'
# graph=facebook.GraphAPI(token)
# profile =graph.get_object('me',fields='name,location')
# print(json.dumps(profile,indent=4))
#print(r.status_code)

#print(r._content)
#print(r._content_consumed)
from flask import Flask
from flask import request
import requests
import facebook
import urllib

import json
#https://teamtreehouse.com/community/can-someone-help-me-understand-flaskname-a-little-better
app = Flask(__name__)

FACEBOOK_APP_ID = '1664841416939079'
FACEBOOK_APP_SECRET = '70e0a8b22eccbab11ee6f3a8306152bd'

@app.route("/")
def hello():
    #here request is request of flask not the requests library and it return the attribute specified 
    code = request.args.get('code')

    # print(code)
    #Exchanging Code for an Access Token
    r=requests.get('https://graph.facebook.com/v2.12/oauth/access_token?client_id={}&redirect_uri={}&client_secret={}&code={}'.format(FACEBOOK_APP_ID,'http://localhost:8080/',FACEBOOK_APP_SECRET,code))
    data = r.json()
    #g=data['content'][0]
    #print(g)
    access_token=data['access_token']
    graph = facebook.GraphAPI(access_token)
    # me is of type dictionary
    me= graph.request('/me')
    id=me.get('id')
    friends= graph.request('/me/friends')
    data_friends=friends['data']
    print(me)
    print(friends)
    print(data_friends)

    return 'Hi pal'

#debug=True print out errors on the web page

app.run(host="0.0.0.0", port=int("8080"), debug=True)



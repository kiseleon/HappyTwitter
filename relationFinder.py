from pythonDB import db_connect
from TwitterAPI import TwitterAPI
from TwitterRelations import TwitterRelations
import secrets
import csv

conn = db_connect()
c = conn.cursor()
CONSUMER_KEY = secrets.get_consumer_key()
CONSUMER_SECRET = secrets.get_consumer_secret()
ACCESS_TOKEN_KEY = secrets.get_access_token_key()
ACCESS_TOKEN_SECRET = secrets.get_access_token_secret()

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, auth_type='oAuth1')

diction_Users = {}

def find_keyword(keyword):

    print keyword

    list = ['joy', 'laughter', 'glad', 'blessed', 'ecstatic', 'excited', 'kindness', 'grace', 'sweetness', 'understanding', 'patience']
    for item in list:
        if item in keyword:
            print "find " + item
            return item

def fill():
    c.execute('SELECT original_tweet_id FROM retweetUsers')
    contents = c.fetchall()
    i = 0
    for row in contents:
        try:
            print "rows ", row
            r = api.request('statuses/show/:%d' % row)
            for item in r:
                reUsers = item['in_reply_to_screen_name']
                tweet = item['text']
                diction_Users[item['user']['screen_name']] = TwitterRelations(num = 0, userList=reUsers, keyword=find_keyword(tweet))
        except:
            r = api.request('statuses/show/:%d' % row)

def grabDB():
    c.execute('SELECT original_tweet_id FROM retweetUsers')
    contents = c.fetchall()
    i = 0
    for row in contents:
        try:
            print "rows ", row
            r = api.request('statuses/show/:%d' % row)
            for item in r:
                twitterRelations = diction_Users[item['user']['screen_name']]
                twitterRelations.setNum_Tweets(i=i + 1)
                diction_Users[item['user']['screen_name']] = twitterRelations
        except:
            r = api.request('statuses/show/:%d' % row)

fill()
grabDB()
conn.close()
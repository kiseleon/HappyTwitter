from pythonDB import db_connect
from TwitterAPI import TwitterAPI
from TwitterRelations import TwitterRelations
import secrets

conn = db_connect()
c = conn.cursor()
CONSUMER_KEY = secrets.get_consumer_key()
CONSUMER_SECRET = secrets.get_consumer_secret()
ACCESS_TOKEN_KEY = secrets.get_access_token_key()
ACCESS_TOKEN_SECRET = secrets.get_access_token_secret()

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, auth_type='oAuth1')

diction_Users = {}

def grabDB():

    c.execute('SELECT original_tweet_id FROM retweetUsers')
    contents = c.fetchall()
    i = 0
    for row in contents:
        try:
            print "rows ", row
            r = api.request('statuses/show/:%d' % row)

            for item in r:
                if(item[''])
                reUsers = item['in_reply_to_status_id']
                list = reUsers
                i = diction_Users[item['user']['screen_name']]
                diction_Users[item['user']['screen_name']] = i+1
        except:
            conn = db_connect()
            r = api.request('statuses/show/:%d' % row)



grabDB()
print diction_Users
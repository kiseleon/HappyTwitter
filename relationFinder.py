from pythonDB import db_connect
from TwitterAPI import TwitterAPI
from TwitterRelations import TwitterRelations
import secrets
import csv
from time import sleep

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

    list = ['joy', 'laughter', 'glad', 'blessed', 'ecstatic', 'excited', 'kindness', 'grace', 'sweetness',
            'understanding', 'patience']
    for item in list:
        if item in keyword.lower():
            print "find " + item
            return item


def fill():
    with open('mapdata.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        keyword_map = {'joy': 1, 'laughter': 2, 'glad': 3, 'blessed': 4, 'ecstatic': 5, 'excited': 6, 'kindness': 7,
                       'grace': 8, 'sweetness': 9, 'understanding': 10, 'patience': 11}

        contents = c.execute('SELECT rtusername, original_tweet_id FROM retweetUsers')

        for row in contents:
            try:
                print "rows ", row[0]
                r = api.request('statuses/show/:%d' % row[1])

                for item in r:
                    reUsers = item['in_reply_to_screen_name']
                    tweet = item['text']
                    username = item['user']['screen_name']
                    keyword = find_keyword(tweet)
                    writer.writerow([username, row[0], keyword, reUsers, keyword_map[keyword]])
            except:
                print "trying again"
                # sleep(900)
                r = api.request('statuses/show/:%d' % row[1])


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

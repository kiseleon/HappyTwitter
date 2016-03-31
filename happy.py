from TwitterAPI import TwitterAPI
import sqlite3
import secrets  # this is the file that stores the secrets
from pythonDB import db_connect

CONSUMER_KEY = secrets.get_consumer_key()
CONSUMER_SECRET = secrets.get_consumer_secret()
ACCESS_TOKEN_KEY = secrets.get_access_token_key()
ACCESS_TOKEN_SECRET = secrets.get_access_token_secret()

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, auth_type='oAuth1')

# r = api.request('application/rate_limit_status')

# r = api.request('statuses/update', {'status': 'Test tweet from Python'})
conn = db_connect()

# r = api.request('search/tweets', {'q': 'happy'})
# for item in r:
# print(item)
keyword = 'joy,laughter,glad,blessed,ecstatic,excited,kindness,grace,sweetness,understanding,patience'

r = api.request('statuses/filter', {'track': [keyword], 'language': 'en'})

while (True):

    try:
        for item in r:
            print(item['text'] if 'text' in item else item)
            if 'text' in item:
                statement = item['text']
                split = statement.split(' ', 2)
                username = split[0]
                tweet = item['text']
                rt_name = item['user']['screen_name']
                tweet_id = item['id']

                """This should split on retweets"""
                if "RT" == split[0] and 'retweeted_status' in item:  # is didn't work here for whatever reason, so == it is
                    username = item['retweeted_status']['user']['screen_name']
                    conn.execute("INSERT INTO retweetUsers (username, rtusername, tweets, keywords, tweet_id, original_tweet_id) VALUES (?, ?, ?, ?, ?, ?)", [username, rt_name, tweet, keyword, tweet_id, item['retweeted_status']['id']])
                    conn.commit()
                else:  # "@" is split[0][0]: # This only grabs tweets that start by referencing another person, whereas we want all non-retweets here
                    conn.execute("INSERT INTO parentUsers (username, tweets, keywords, tweet_id) VALUES (?, ?, ?, ?)", [rt_name, tweet, keyword, tweet_id])
                    conn.commit()
    except:
        conn = db_connect()
        r = api.request('statuses/filter', {'track': [keyword], 'language': 'en'})


print("records created successful")
conn.close()


        # Print HTTP status code (=200 when no errors).

        # print(r.status_code)

        # Print the raw response.
        # print(r.text)

# Parse the JSON response.
# j = r.response.json()
# print(j['resources']['search'])

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
keyword = 'kindness'

r = api.request('statuses/filter', {'track': [keyword], 'language': 'en'})
rt = 0
for item in r:
    print(item['text'] if 'text' in item else item)
    statement = item['text']
    split = statement.split(' ', 1)
    username = split[0]
    tweet = split[1]
    print username
    print tweet
    if "RT" == split[0]:
        rt = 1
        conn.execute("INSERT INTO parentUsers (username, tweets, keywords, retweet) \
                     VALUES (" + username + ","+ str(tweet) +","+keyword+","+rt+")");
    elif "@" == split[0][0]:
        rt = 0
        conn.execute("INSERT INTO parentUsers (username, tweets, keywords, retweet) \
                     VALUES (" + username + ","+ str(tweet) +","+keyword+","+rt+")");
    conn.commit()
    print "records created successful"
    conn.close()


        # Print HTTP status code (=200 when no errors).

        # print(r.status_code)

        # Print the raw response.
        # print(r.text)

# Parse the JSON response.
# j = r.response.json()
# print(j['resources']['search'])

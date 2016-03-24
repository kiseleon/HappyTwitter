from TwitterAPI import TwitterAPI
import sqlite3
import secrets  # this is the file that stores the secrets

CONSUMER_KEY = secrets.get_consumer_key()
CONSUMER_SECRET = secrets.get_consumer_secret()
ACCESS_TOKEN_KEY = secrets.get_access_token_key()
ACCESS_TOKEN_SECRET = secrets.get_access_token_secret()

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, auth_type='oAuth1')

#r = api.request('application/rate_limit_status')

#r = api.request('statuses/update', {'status': 'Test tweet from Python'})


#r = api.request('search/tweets', {'q': 'happy'})
#for item in r:
#    print(item)

r = api.request('statuses/filter', {'track': ['good friend'], 'language': 'en'})

for item in r:
    print(item['text'] if 'text' in item else item)

# Print HTTP status code (=200 when no errors).

#print(r.status_code)

# Print the raw response.
#print(r.text)

# Parse the JSON response.
#j = r.response.json()
#print(j['resources']['search'])

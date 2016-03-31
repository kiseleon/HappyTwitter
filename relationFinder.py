from pythonDB import db_connect
import TwitterAPI
from TwitterRelations import TwitterRelations

conn = db_connect()
c = conn.cursor()


def grabDB():

    c.execute('SELECT original_tweet_id FROM retweetUsers')
    contents = c.fetchall()

    for row in contents:
        print "rows ", row


grabDB()
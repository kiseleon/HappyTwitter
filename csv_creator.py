import csv
from pythonDB import db_connect


# open the database
connect = db_connect()

# to use for fetching rows
cursor = connect.execute("SELECT username, rtusername from retweetUsers")

with open('mapdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in cursor:
        writer.writerow([row[0], row[1]])



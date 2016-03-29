create table retweetUsers
	(
	rtID INTEGER PRIMARY KEY AUTOINCREMENT,
	username varchar(255) NOT NULL,
	rtusername varchar(255) NOT NULL,
	tweets BLOB NOT NULL,
	keywords varchar(40),
	retweets INTEGER,
	FOREIGN KEY(retweets) REFERENCES parentUsers(rootUsersID));
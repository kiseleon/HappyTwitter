create table retweetUsers
	(
	rootUsersID INTEGER PRIMARY KEY AUTOINCREMENT,
	username varchar(255) NOT NULL,
	tweets varchar(150) NOT NULL,
	keywords varchar(40),
	retweet tinyint(1));

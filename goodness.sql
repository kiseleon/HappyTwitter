create table rootUsers
	(
	rootUsersID int NOT NULL PRIMARY KEY,
	username varchar(255) NOT NULL,
	tweets varchar(150) NOT NULL,
	keywords varchar(40),
	retweet tinyint(1));

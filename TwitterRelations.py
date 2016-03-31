class TwitterRelations:
    def __init__(self, numberTweets, userList):
        self.user_list = userList
        self.num_tweets = numberTweets

    def getUser_Tweets(self):
       return self.num_tweets

    def getUser_List(self):
        return self.user_list

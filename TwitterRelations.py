class TwitterRelations:
    def __init__(self, numberTweets, userList, keyword):
        self.user_list = userList
        self.num_tweets = numberTweets
        self.keyword = keyword

    def getUser_Tweets(self):
       return self.num_tweets

    def getUser_List(self):
        return self.user_list

    def setUser_List(self,listItem):
        self.user_list = listItem
        return

    def setNum_Tweets(self, num_tweets):
        self.num_tweets = num_tweets
        return

    def get_Keyword(self):
        return self.keyword

    def set_Keyword(self, keyword):
        self.num_tweets = keyword
        return
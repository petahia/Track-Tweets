import pandas as pd
from source.load_data import LoadData

class DataAnalyzer:
    def __init__(self,data):
        self.data = LoadData()

    # amount of tweets for each category
    def tweets_amount(self):
        amount_define = self.data.groupby(['Biased']).count()
        amount_not_define = self.data[self.data["Biased"] != (1 or 0)].count()
        amount_any = self.data['TweetID'].count()
        return amount_define,amount_not_define,amount_any

    # the avarage length of tweets
    df1 = df[df['Biased'] == 1]
    df0 = df[df['Biased'] == 0]
    tweets = df['Text'].apply(lambda x: str(x).split())
    rows = tweets.count()
    tweets1 = df1['Text'].apply(lambda x: str(x).split())
    rows1 = tweets1.count()
    tweets0 = df0['Text'].apply(lambda x: str(x).split())
    rows0 = tweets0.count()

    def avarage_of_lens(df):
        amount = 0
        amount1 = 0
        amount0 = 0
        for tweet in tweets1:
            amount1 += len(tweet)
    
        for tweet in tweets0:
            amount0 += len(tweet)
    
        for tweet in tweets:
            amount += len(tweet)
    
        avarage1 = amount1 / rows1
        avarage0 = amount0 / rows0
        avarage = amount / rows
    
        return float(avarage1),float(avarage0), float(avarage)


    # 3 tweets with the most characters
    def three_longest_tweets(df):
        df1 = df[df['Biased'] == 1].sort_values(by='Text', key=lambda x: len(str(x)), asceding=False).head(3)
        df0 = df[df['Biased'] == 0].sort_values(by='Text', key=lambda x: len(str(x)), asceding=False).head(3)

        return df1, df0


    # ten_common_tweets
    def ten_common_tweets(df):
        ten_common_tweets = df['Text'].apply(lambda x: str(x).split()).sort_values(by='Text',key=lambda x: len(x)).head(10)
        return ten_common_tweets


    # num_of_uppercase_words
    def num_of_uppercase(df):
        uppercase1 = df1['Text'].apply(lambda x: str(x).split()).isupper().count()
        uppercase0 = df0['Text'].apply(lambda x: str(x).split()).isupper().count()
        total = uppercase1 + uppercase0

        return uppercase1,uppercase0,total



        
    








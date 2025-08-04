import pandas as pd

class LoadData:
    def __init__(self,data):
        self.data = data

df = LoadData(pd.read_csv('file:/Users/petahiam/PycharmProjects/TrackTweets/data/tweets_dataset.csv'))





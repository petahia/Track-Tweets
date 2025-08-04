import pandas as pd
from numpy._core.strings import lower
from source.load_data import LoadData


class Cleaner:

    def __init__(self,data):
        self.data = LoadData()

    # the relevant colomns, without commas, lower case only, export to csv file in result directory
    def cleaning(self):
        new_df = self.data['Text', 'Biased']]
        new_df = new_df['Text'].replace(',', '', inplace=True)
        new_df = new_df['Text'].apply(lambda x: lower(x), inplace=True)
        new_df = new_df[new_df['Biased'].isin([1, 0])]
        print(new_df)
        new_df.to_csv('file:/Users/petahiam/PycharmProjects/TrackTweets/results/tweets_dataset_cleaned.csv')






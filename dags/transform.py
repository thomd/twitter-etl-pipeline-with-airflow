import pandas as pd

def clean_twitter_data():
    df = pd.read_csv('tweets.csv')

    # remove non-ascii character
    df.text.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
    df.location.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
    df.to_csv('tweets.csv', index=False)


import pandas as pd

def clean_twitter_data():
    df = pd.read_csv('tweets.csv')

    # format datetime for postgresql
    df.datetime = pd.to_datetime(df.datetime).dt.strftime('%Y-%m-%d %H:%M:%S')

    # remove non-ascii character
    df.text.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
    df.source.replace({r'[^\x00-\x7F]+': ''}, regex=True, inplace=True)
    df.location.replace({r'[^\x00-\x7F]+': None}, regex=True, inplace=True)

    # replace newline, tabs and carriage-return
    df.replace({r'\r+|\n+|\t+': ' '}, regex=True, inplace=True)

    # fill missing data
    df.location.fillna(value='NA', inplace=True)

    df.to_csv('tweets.csv', index=False, sep ='\t', header=None)

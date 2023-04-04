import pandas as pd
import snscrape.modules.twitter as sntwitter

def extract_from_twitter():
    tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('ChatGPT since:2023-01-14').get_items()):
        if i > 100:
            break
        tweets.append([tweet.date, tweet.user.username, tweet.rawContent, tweet.sourceLabel, tweet.user.location])

    tweets_df = pd.DataFrame(tweets, columns=['datetime', 'username', 'text', 'source', 'location'])
    tweets_df.to_csv('tweets.csv', index=False)


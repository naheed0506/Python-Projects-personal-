import tweepy
from textblob import TextBlob

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def fetch_tweets(query, count=100):
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(count):
        tweets.append(tweet.text)
    return tweets

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def main():
    query = input("Enter search query: ")
    tweets = fetch_tweets(query, count=100)
    
    positive_tweets = sum(1 for tweet in tweets if analyze_sentiment(tweet) > 0)
    negative_tweets = sum(1 for tweet in tweets if analyze_sentiment(tweet) < 0)
    neutral_tweets = len(tweets) - positive_tweets - negative_tweets
    
    print("Sentiment Analysis Results:")
    print(f"Positive Tweets: {positive_tweets}")
    print(f"Negative Tweets: {negative_tweets}")
    print(f"Neutral Tweets: {neutral_tweets}")

if __name__ == "__main__":
    main()

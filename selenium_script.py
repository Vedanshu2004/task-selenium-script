import tweepy
from pymongo import MongoClient
import datetime


api_key = 'fmktQkmnh8ZA2QeOnWr37Kudk'
api_secret_key = 'nM5oP1lLiEjmhOazANudId3CumIboSD7qpHHJ7DhosJROapxCX'
access_token = '1687453632927830016-WSFPpDjVwtW3csjr5W5VgfHw2Nr0rX'
access_token_secret = 'iLGGpxZTVFVVDPYxsrnsVapb0PBJx5Vsl1WZw3x5ZB6pu'


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def fetch_trending_topics(woeid):
    try:
        trends = api.get_place_trends(id=woeid)
        trending_topics = [trend['name'] for trend in trends[0]['trends'][:5]]
        return trending_topics
    except Exception as e:
        print(f"Error fetching trends: {e}")
        return None

def store_trending_topics_in_mongo(trending_topics):
    try:
        
        client = MongoClient('mongodb://localhost:27017/')
        db = client["trending_topics_db"]
        collection = db["trends"]

        
        record = {
            "trends": trending_topics,
            "date": datetime.datetime.now(),
        }

        
        collection.insert_one(record)
        print("Trending topics saved to MongoDB.")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

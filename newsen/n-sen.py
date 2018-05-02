import geopandas as gpd
from shapely.geometry import Point, Polygon
import couchdb
import json
import sentiment_mod as sentiment
COUCHDB_ADDRESS = 'http://admin:admin@localhost:5984/'
COUCHDB_TWEETS_DBNAME = 'twitter'
couch = couchdb.Server()
couch = couchdb.Server(COUCHDB_ADDRESS)
db = couch[COUCHDB_TWEETS_DBNAME]
while True:
  mango = {'selector':{'_id':{"$gt":None}}, "sort":[{"_id":"asc}], "limit":1000, "skip": counter*1000}
  results = list(db.find(mango))
  if len(results) == 0:
      break
  for result in results:
      tweet_id = result['_id']
      tweet = result['text']                                                 
      doc = db[tweet_id]
      doc['SENTIMENT'] = sentiment.sentiment(tweet)
      db[tweet_id] = doc
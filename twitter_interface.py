#! /usr/bin/env python

from twitter import Twitter, OAuth, TwitterHTTPError

from pprint import pprint
import json

def import_configs():
	f = open("config.json", "r")
	configs = json.loads(f.read())
	return configs

def search_tweets(t, q, count=100):
	return t.search.tweets(q=q, result_type='recent', count=count)

def main(configs):
	t = Twitter(auth=OAuth(configs['OAUTH_TOKEN'], 
			configs['OAUTH_SECRET'],
			configs['CONSUMER_KEY'], 
			configs['CONSUMER_SECRET']))
	return search_tweets(t, '#kanye')

if __name__ == "__main__":
	configs = import_configs()
	pprint(main(configs))

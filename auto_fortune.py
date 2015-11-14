'''
auto_fortune.py 

a twitter bot that pulls a random tarot card and creates a fortune to post.

useage: python main.py 

v0.1 - 11/11/2015 Aaron Schuman
'''

import tweepy
import time
import random
import json

# method for getting twitter api obj setup that returns obj?
def  create_api_from_file(path):
	f = open(path, "r")
	auth_keys = json.load(f)

	auth = tweepy.OAuthHandler(auth_keys['consumer_key'], auth_keys['consumer_secret'])
	auth.set_access_token(auth_keys['access_key'], auth_keys['access_secret'])

	return tweepy.API(auth)

# method to create fortune
def make_fortune(path):
	f = open(path, "r")
	words = json.load(f)
	pre_text = "%s %s %s %s at %s." % (random.choice(words['noun_singular']),
										random.choice(words['command']), 
										random.choice(words['verb']), 
										random.choice(words['adjective']),
										random.choice(words['place']))
	# pre_text = '%s %s %s.' % (random.choice(), random.choice(does), random.choice(action))
	return ' '.join(word[0].upper() + word[1:] for word in pre_text.split())

api =  create_api_from_file('auth.json')

while True:
	fortune = make_fortune('words.json')
	print fortune
	# post post post
	api.update_status(status=fortune)
	time.sleep(3)

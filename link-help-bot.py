#!/usr/bin/python
# coding=utf-8
import praw
import config
import time 
import os
import string
import requests
import random

def bot_login():
	print "Loggin in..."
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "Link-Help-Bot")
	print "Logged in!"
	
	return r

response = ["[Here you go.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", 
			"[Here's the link.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)", 
			"[You can find that here.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
			"[I think this is what you're looking for.](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"]

def run_bot(r, comments_replied_to):
	print "Obtaining Comments..."

	for comment in r.subreddit(config.reddit_sub).comments(limit=None):
		if "link?" in comment.body and comment.id not in comments_replied_to and comment.author and comment.author != r.user.me():
			comments_replied_to.append(comment.id)	
			secure_random = random.SystemRandom()
			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
			comment_reply = (secure_random.choice(response))
			print "Replied to comment (sub1): " + comment.id
			comment.reply(comment_reply)

	for comment in r.subreddit(config.reddit_sub).comments(limit=None):
		if "Link?" in comment.body and comment.id not in comments_replied_to and comment.author and comment.author != r.user.me():
			comments_replied_to.append(comment.id)	
			secure_random = random.SystemRandom()
			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
			comment_reply = (secure_random.choice(response))
			print "Replied to comment (sub1): " + comment.id
			comment.reply(comment_reply)

	print "Searching Comments..."
	
	time.sleep(1)

def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to
		
r = bot_login()
comments_replied_to = get_saved_comments()
print comments_replied_to

while True:
	run_bot(r, comments_replied_to)
	
		

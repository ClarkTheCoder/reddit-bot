import praw 
import config 

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.secret_id,
			user_agent = "Clark's Snekbot")
	print "logged in"

	return r 

def run_bot(r):
	print "obtaining 25 comments"
	for comment in r.subreddit('indianpeoplefacebook').comments(limit=25):
		if "real" in comment.body:
			print "string with \"real\" found!" + comment.id
			comment.reply("Is anything real?")
			print "replied to comment" + comment.id

r = bot_login()
run_bot(r)

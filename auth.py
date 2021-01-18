#! /usr/bin/python3
import praw
import os

client_id = os.environ.get('SELF_HELP_CLIENT_ID')
client_secret = os.environ.get('SELF_HELP_CLIENT_SECRET')

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='selfhelp2020')


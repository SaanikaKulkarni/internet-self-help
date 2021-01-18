import praw
from auth import reddit
import pandas as pd 
import datetime as dt 
import numpy as np 
import os
import datetime

data_dict={
        "id": [],
        "body":[],
        "self":[],
        "orig":[],
        "score":[],
        "author":[],
        "title":[],
        "time":[],
        "subreddit_name":[],
        "body_length":[],
        "title_length":[]
    }

def get_subreddits(count=200):
    """Gets the top 200 submissions from 7 self help subreddits:
        1. r/selfimprovement
        2. r/zenhabits
        3. r/GetMotivated
        4. r/howtonotgiveafuck
        5. r/productivity
        6. r/GetDisciplined
        7. r/DecidingToBeBetter

        returns: submission instances of these subreddits using praw
    """
    sub_self_improv = reddit.subreddit('selfimprovement').top(limit=count)
    sub_zenhabits = reddit.subreddit('zenhabits').top(limit=count)
    sub_get_motiv = reddit.subreddit('GetMotivated').top(limit=count)
    sub_how_to_not = reddit.subreddit('howtonotgiveafuck').top(limit=count)
    sub_prod = reddit.subreddit('productivity').top(limit=count)
    sub_get_dis = reddit.subreddit('GetDisciplined').top(limit=count)
    sub_be_better = reddit.subreddit('DecidingToBeBetter').top(limit=count)
    return sub_self_improv, sub_zenhabits, sub_get_motiv, sub_how_to_not,sub_prod,sub_get_dis, sub_be_better

def to_date(utc_time):
    """
    Converts UTC time of when the comment was posted to datetime

    returns: Date as a string in YYYY-MM format
    """
    dt = datetime.datetime.utcfromtimestamp(utc_time)
    final_dt = str(dt.year)+'-'+str(dt.month)
    return final_dt

def create_raw_df():
    subreddits = list(get_subreddits(1000))
    for subred in subreddits:
        make_dict(subred)
    df = pd.DataFrame.from_dict(data_dict)
    return df

    


def make_dict(subred):
    """
    Maps aspects of subreddit submission:
    1. id
    2. body
    3. self (bool)
    4. original (bool)
    5. score
    6. author
    7. title
    8. time (in YYYY-MM)
    9. subreddit it belongs to
    10. length of the body text

    returns: a dictionary of these values
    """
    
    for submission in subred:
        data_dict["id"].append(submission.id)
        data_dict["self"].append(submission.is_self)
        data_dict["orig"].append(submission.is_original_content)
        data_dict["score"].append(submission.score)
        data_dict["body"].append(submission.selftext)
        data_dict["author"].append(submission.author)
        data_dict["title"].append(submission.title)
        data_dict["subreddit_name"].append(submission.subreddit.display_name)
        data_dict["time"].append(to_date(submission.created_utc))
        data_dict["body_length"].append(len(submission.selftext.split()))
        data_dict["title_length"].append(len(submission.title.split()))

    return data_dict



df =create_raw_df()


# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:53:33 2019

@author: sapta
"""
#%%
import praw

#%%
reddit = praw.Reddit(client_id='Type_in_ID',
                     client_secret='Type_in_code', password='Type_in_password',
                     user_agent='name of app', username='JewwBacccaaa')
#print(reddit.user.me())
subreddit = reddit.subreddit('Name_of_subreddit')

#%%
hot_python = subreddit.controversial("day",limit=5)
for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                           submission.ups,
                                                                           submission.downs,
                                                                           submission.visited))
#%% The posts they commented in
for comment in reddit.redditor('name').comments.new(limit=10):
    print(comment.body.split('\n\n', 1)[0][0:180])
# What kind of popsts did they submit
#for submission in reddit.redditor('DiamondsOnTheFloor').submissions.top('all'):
#    print(submission.title)         
#%%        
comments = submission.comments
for comment in comments:
    print(20*'-')
    print(comment.body)
    if len(comment.replies) > 0:
        for reply in comment.replies:
            print('REPLY:')
            print("\t"+reply.body)
#%%    
import praw
import re

#create praw reddit object using bot1 profile
reddit_inst = praw.Reddit(
    "bot1",
    user_agent="postreader"
)

#find sub that you want to look at or post in
sub = reddit_inst.subreddit("wallstreetbets")

#get posts from sub -- note that the first posts can be pinned posts by the sub
posts = sub.hot(limit=5)

#look at each post and identify key words
for post in posts:
    if post.stickied:
        continue
    print(post.title)
    print(post.body)

def extract_info(text):
    pattern = r'\b[A-Z]{1,5}\b' 
    tickers = re.findall(pattern, text)
    return tickers
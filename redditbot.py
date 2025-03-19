import praw

#create praw reddit object using bot1 profile
reddit_inst = praw.Reddit(
    "bot1",
    user_agent="postreader"
)

#print(reddit_inst.user.me())

#find sub that you want to look at or post in
sub = reddit_inst.subreddit("bots")


#get posts from sub -- note that the first posts can be pinned posts by the sub
posts = sub.hot(limit=5)

#look at each post and identify key words
for post in posts:
    print(post.title)
    post.comments.replace_more(limit=None)
    for comment in post.comments.list():
        print(comment.body)
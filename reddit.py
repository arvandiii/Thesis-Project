import time
import praw


reddit = praw.Reddit(
    client_id="Hz2zkQJCMOiFVifmyeGzrg",
    client_secret="2_ydmLRpoLBtuqOx_6WNoq1j59BZXw",
    user_agent="Emergency Management",
)


i = 0

params = {'sort':'relevance', 'limit':None}

for submission in reddit.subreddit("RobinHoodPennyStocks").search("AUMN is looking like it’s gonna keep going up", **params):
    for attr in dir(submission):
        if not attr.startswith('_'):
            value = getattr(submission, attr)
            print(f"{attr}: {value}")
    break
import time
import praw


reddit = praw.Reddit(
    client_id="Hz2zkQJCMOiFVifmyeGzrg",
    client_secret="2_ydmLRpoLBtuqOx_6WNoq1j59BZXw",
    user_agent="Emergency Management",
)


i = 0

params = {'sort':'new', 'limit':None}



for submission in reddit.subreddit("all").search("kelowna", **params):
    print('====================================')
    print(submission.title)
    print(submission.selftext)
    for c in submission.comments:
        print('comment:', c.body)
    created_at = submission.created_utc
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(created_at)))

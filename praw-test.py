#praw test

import praw, os

userAgent = "web:compoundingcarlbot:v1.0.0 (by u/CompoundingCarlBot)"
clientId = "DO4eYTlDI2J1ug"
secretKey = os.environ["REDDIT_SECRET_KEY"]

username = "CompoundingCarlBot"
password = os.environ["COMPOUNDING_CARL_PASSWORD"]

reddit = praw.Reddit(client_id=clientId,
                     client_secret=secretKey,
                     password=password,
                     user_agent=userAgent,
                     username=username)

print(reddit.user.me())

sub = reddit.subreddit('personalfinance')
print(sub.display_name)
print(sub.title)

# firm up UI via reddit (start, update, stop)
# agree on wire protocol (http) between bot and reddit, and bot and django back end
# run daily update process

import praw
import pdb
import re
import os

# create reddit instance
reddit = praw.Reddit("bot1")

# subreddit for bot
subreddit = reddit.subreddit("armenia").hot(limit=5)

# posts replied to file
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))

# comments replied to file
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []
else:
    with open("comments_replied_to.txt", "r") as f:
       comments_replied_to = f.read()
       comments_replied_to = comments_replied_to.split("\n")
       comments_replied_to = list(filter(None, comments_replied_to))

# positive adjectives list
with open("positive_adjectives.txt", "r") as f:
       positive_adjectives = f.read()

subreddit = reddit.subreddit('armenia')

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search(positive_adjectives, submission.title, re.IGNORECASE):
            submission.reply("I agree with your post! All about Love and Support! -ArmeniaBot")
            print("ArmeniaBot replied to '" + submission.title + "'")
            # add to list of posts replied to
            posts_replied_to.append(submission.id)

    # reply to one comment which contains the compliment adjectives from the list
    for comment in submission.comments:
        if comment.id not in comments_replied_to:
            comment.reply("I agree with your comment! Love and support! -ArmeniaBot")
            print("ArmeniaBot replied to " + str(comment.author) + "'s comment: " + comment.body)
            comments_replied_to.append(comment.id)
            print("-------------------")
        break


# add all post_ids to the text file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

# add all comment_ids to the text file
with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")
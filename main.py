import praw
import random

reddit = praw.Reddit(client_id="XZ6OzCHkiCabJA",
                     client_secret="m47gGnWcsCiVABSp9clCZaBawW6-Ng",
                     user_agent="<console_Programmers>",
                     username="PrabhuCS_Programmer",
                     password="Pr8009747730"
                     )


list = ["Programming is not about what you know, it is about what you can figure out.",
        "The only way to learn a new programming language is by writing programs in it",
        "Sometimes it's better to leave something alone, to pause, and that's very true of programming.",
        "Testing leads to failure, and failure leads to understanding.",
        "The best error message is the one that never shows up."]

subreddit = reddit.subreddit("computerscience")
for post in subreddit.hot(limit=10):
    #print('1')
    for comments in post.comments:
        if hasattr(comments,"body"):
            comment_lower = comments.body.lower()
            if " programming " in comment_lower:
                random_index = random.randint(0, len(list)-1)
                comments.reply(list[random_index])

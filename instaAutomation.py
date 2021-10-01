# Step 1 install libraries
# pip install instabot

# Importing Libraries
from instabot import Bot
import os
import glob
from tqdm.std import tqdm

# Filtration
bot = Bot(max_follows_per_day=150, follow_delay=60, filter_previously_followed=True, filter_verified_accounts=True, filter_private_users=True, filter_business_accounts=True)

# This line will read password from the file named password.txt
password_file = open("password.txt", "r")
password = password_file.read()

#Enter your username here
bot.login(username="username", password=password)

# Enter user list here to fetch their photos
user_list = ["deepikapadukone", "priyankachopra",
 "urvashirautela", "dishapatani", "kiaraaliaadvani", "norafatehi", "aliaabhatt",]

# Iterate over the user list
for user in user_list:
    medias = bot.get_user_medias(user, filtration=False)
    print (medias)
    post1 = medias[0]
    post2 = medias[1]

    likers = bot.get_media_likers(post1)

    cnt = 0

# getting Likes of the post and who like it
    for liker in tqdm(likers):
        if cnt < 10:
            print (bot.get_username_from_user_id(liker))
            bot.follow(liker)
            cnt += 1

    likers = bot.get_media_likers(post2)

    cnt = 0

# Here we Follow the likers of the post
    for liker in tqdm(likers):
        if cnt < 10:
            print (bot.get_username_from_user_id(liker))
            bot.follow(liker)
            cnt += 1

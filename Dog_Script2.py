import os
import shutil
from PIL import Image
import random
import tweepy


#Removed access credentials

os.chdir('/Users/lukaissciandra/Desktop/Python/Dog_Breeds/images/images')
dictionary = {}
i = 0
dataset_length = 0
for folder,subfolders,files in os.walk(os.getcwd()):
    for subfold in subfolders:
        i += 1
        dictionary[i] = subfold
num = random.randint(1,120)

newpath = '/Users/lukaissciandra/Desktop/Python/Dog_Breeds/images/images' + '/' + dictionary[num]

os.chdir(newpath)
currentbreed = newpath[72:]
currentbreed = currentbreed.replace('_',' ')
tweet_text = currentbreed
paths = {}
for j in range(1,5,1):
    k = 0
    images = {}
    for folder,subfolders, files in os.walk(os.getcwd()):
        for file in files:
            k += 1
            images[k] = file
        
        
    value = random.randint(1,k)
    picturepath = newpath + '/' + images[value]
    paths[j] = picturepath


auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

images = (paths[1], paths[2], paths[3], paths[4])
media_ids = [api.media_upload(i).media_id_string for i in images]
api.update_status(status=tweet_text, media_ids=media_ids)
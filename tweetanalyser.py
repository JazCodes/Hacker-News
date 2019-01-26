# class TweetAnalyser:
#     def __init__(self, good_words, bad_words):
#         self.good_words = good_words
#         self.bad_words = bad_words
    
    
    

#     def good_in_tweets(self, tweets, words):
#         words = tweets.split()
    
#         good = 0
#         bad = 0
        
#         for word in words:
#             if word in self.good_words:
#                 good += 1
#             if word in self.bad_words:
#                 bad +=1
#         if(good > bad):
#             print("good")
#         if(bad > good):
#             print("bad")
#         else:
#             print("neutral")


#     def check_tweet(self, tweet):
#     	self.tweet = tweet

#     	tweet = input("whats your tweet")
#     	print("your tweet is -  " + tweet)
    	
        
        






with open("goodwords.txt", "r") as f:
    good_words = f.readlines()

with open("badwords.txt", "r") as f:
    bad_words = f.readlines()

with open("tweets.csv", "r") as f:
    tweets = f.readlines()

a = [x.strip() for x in good_words]
b = [x.strip() for x in bad_words]
c = [x.split(",")[3].strip() for x in tweets][1:]

print(c[0])

gt = []
bt = []

for i in range(0,10):
    gc = 0
    bc = 0

    current_tweet = c[i].split(" ")

    for j in range(0, len(current_tweet)):
        current_word = current_tweet[j]
        if current_word in a:
            gc += 1
        elif current_word in b:
            bc += 1

    if gc > bc:
        sentiment = 'good'
    elif gc < bc:
        sentiment = 'bad'
    else:
        sentiment = 'inconclusive'
    print(current_tweet, sentiment)

import requests

from flask import Flask 
from flask import render_template

app =Flask(__name__)


@app.route('/')
def HackerNewsCode():
	response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

# Get top 5 ids
	top_five_ids = response.json()[:5]

# Fetch top 5 stories

	stories = []

	for top_id in top_five_ids:
	curr_story_api_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)
	curr_story = requests.get(curr_story_api_url)
	stories.append(curr_story.json())

	listOfStories = []

	for story in stories:
	title = story['title'] 
	comments = [] 
	dictionary = {}  

	for kid in story['kids'][:5]:
	   
	   kid_url = requests.get('https://hacker-news.firebaseio.com/v0/item/' +str(kid)+'.json?print=pretty')
	   comment = kid_url.json()['text'] 
	   comments.append(comment) 
	   dictionary[title] = comments 
	   listOfStories.append(dictionary) 


class HackerNews:
	with open('goodwords.txt', 'r') as open_pos:
		positive_vocab=open_pos.readlines()

	with open('badwords.txt', 'r') as open_neg:
		negative_vocab=open_neg.readlines()
	
	def __init__(self, positive_vocab, negative_vocab):
		self.positive_vocab = positive_vocab
		self.negative_vocab = negative_vocab

	
	def analyze_news(hacker):
		words = hacker.split()

		num_positive_vocab = 0 
		num_negative_vocab = 0 
		for word in words:
		 
			if word in positive_vocab:
				num_positive_vocab += 1
			elif word in negative_vocab:
				num_negative_vocab += 1 

		if num_positive_vocab > num_negative_vocab:
			return "positive"

		elif num_positive_vocab < num_negative_vocab:
			return "negative"
		else: 
			return "inconclusive" 

		for sentence in listOfStories:
			hacker = sentence.split(",")[3].strip()

			analyze_news(hacker)
	
	hacker = input("What do you want to analyze?")
	analyze_news(hacker)
	print(analyze_news(hacker))
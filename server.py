from flask import Flask, jsonify
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
	response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')

	top_five_ids = response.json()[:10]

	print('Top five ids:', top_five_ids)

	comments = {}

	stories = []

	for id in top_five_ids:
	    curr_story_api_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)
	    curr_story = requests.get(curr_story_api_url)
	    stories.append(curr_story.json())


	for story in stories:
		if 'kids' in story:
		    comment_ids = story['kids'][:100]
		    title = story['title']
		    comments[title] = []


	for comment_id in comment_ids:
	    curr_comment_api_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(id)
	    curr_comment = requests.get(curr_comment_api_url)
	    comments[title].append(curr_comment.json())

	return jsonify(comments)



if __name__ == '__main__':
	app.run()
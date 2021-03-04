import requests
from flask import Flask, render_template, request
import json
import os
from operator import itemgetter

os.system('clear')

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


base_url = 'https://www.reddit.com/'
data = {
    'grant_type': 'password',
    'username': 'Comprehensive_Bag583',
    'password': 'hejoreddit!!'
}
auth = requests.auth.HTTPBasicAuth('bp-j2PhaT2f7bw', 'PSi17BKQ2WPeVamim1XB1N4ZXtC6_Q')
r = requests.post(base_url+'api/v1/access_token', data=data, headers=headers, auth=auth)
d = r.json()


token = 'bearer '+d['access_token']
oauth_url = 'https://oauth.reddit.com/api/v1/me'
headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
response = requests.get(oauth_url, headers=headers)
#if response.status_code == 200:
#    print()


LIMIT = 6


api_url = 'https://oauth.reddit.com'
payload = {'limit': LIMIT, 't': 'month'}
'''
with open('test.json', 'w') as file:
    json.dump(values, file)
for i in range(LIMIT):
    #print(f"\n#{i+1}\n{values['data']['children'][i]['data']['title']}\n")
'''



"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django",
    "python",
    "flask",
    "node"
]


app = Flask("DayEleven")


@app.route('/')
def home():
    return render_template('home.html', subreddits=subreddits)


@app.route('/read')
def read():
    selecteds = request.args.to_dict().keys()
    posts = []
    for selected in selecteds:
        response = requests.get(f"{api_url}/r/{selected}/top/", headers=headers, params=payload)
        with open(f"./save_json/subreddit_{selected}.json", 'w') as file:
            json.dump(response.json(), file, indent=4)
        for i in range(LIMIT):
            sub_title = f"r/{selected}"
            title = response.json()['data']['children'][i]['data']['title']
            link = base_url + response.json()['data']['children'][i]['data']['permalink'][1:]
            upvotes = response.json()['data']['children'][i]['data']['ups']
            post = {'sub_title': sub_title, 'title': title, 'link': link, 'upvotes': upvotes}
            posts.append(post)
            print(f"{i+1} {post['sub_title']}\n{post['title']}\n{post['link']}\n{post['upvotes']}")
    posts = sorted(posts, key=itemgetter('upvotes'), reverse=True)
    return render_template('read.html', selecteds=selecteds, posts=posts)


app.run(host="0.0.0.0")
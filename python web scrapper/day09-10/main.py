import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"
# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"
# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

comments_of_story = f"{base_url}/search?tags=comment,story_"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"


db = {'popular': None, 'new': None}
app = Flask("DayNine")


def get_json_dict_obj(url):
    r = requests.get(url)
    json_dict = r.json()
    return json_dict


def search_news(id):
    newss_list = db['popular']
    for news in newss_list:
        if id == news['object_id']:
            return news
    newss_list = db['new']
    for news in newss_list:
        if id == news['object_id']:
            return news


def get_news(news_object):
    detail_url = make_detail_url(news_object['object_id'])
    news_json = get_json_dict_obj(detail_url)
    news = {
        'title': news_json['title'],
        'link': news_json['url'],
        'points': news_json['points'],
        'author': news_json['author'],
        'num_comments': news_object['num_comments'],
        'object_id': news_object['object_id']
    }
    return news


def get_news_list(news_type_url):
    if news_type_url == popular and db['popular'] is not None:
        return db['popular']
    if news_type_url == new and db['new'] is not None:
        return db['new']
    #############################################################
    news_raw_list = []
    news_list = []
    json_dicts = get_json_dict_obj(news_type_url)
    for i in range(20):
        news_raw = {
            'object_id': json_dicts['hits'][i]['objectID'],
            'num_comments': json_dicts['hits'][i]['num_comments']
        }
        news_raw_list.append(news_raw)
    for i, news_raw in enumerate(news_raw_list):
        news = get_news(news_raw)
        news_list.append(news)
        print(f"appending news.. {i+1}/{len(news_raw_list)}")
    #############################################################
    if news_type_url == popular:
        db['popular'] = news_list
    if news_type_url == new:
        db['new'] = news_list
    return news_list


def get_comment_list(comments_url):
    comments_dict_obj = get_json_dict_obj(comments_url)
    last_page = comments_dict_obj['nbPages']
    comment_list = []
    for page in reversed(range(last_page)):
        url = f"{comments_url}&page={page}"
        comments_json_dict = get_json_dict_obj(url)
        max_hits = len(comments_json_dict['hits'])
        for i in reversed(range(max_hits)):
            author = comments_json_dict['hits'][i]['author']
            comment_text = comments_json_dict['hits'][i]['comment_text']
            comment = {'author': author, 'comment_text': comment_text}
            comment_list.append(comment)
            #print(f"\n{author}\n{comment_text}\n")
            print(f"appending comments.. {i+1}")
    return comment_list


@app.route('/')
def home():
    order_by = request.args.get('order_by')
    if order_by == 'new':
        news_type = new
    else:
        news_type = popular
    news_list = get_news_list(news_type)
    print(len(news_list))
    return render_template('index.html', news_list=news_list, news_type=news_type)


@app.route('/<id>')
def detail(id):
    news = search_news(id)
    comments_url = f"{comments_of_story}{id}"
    comment_list = get_comment_list(comments_url)
    #print(f"\n{news}\n")
    return render_template('detail.html', news=news, comment_list=comment_list, none=None)


app.run(host="0.0.0.0")
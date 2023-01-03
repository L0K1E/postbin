from flask import render_template, request, Blueprint
from flaskapp.models import Post
from flaskapp import newsapi
import json
import requests
import datetime

main = Blueprint('main', __name__)


@main.route('/')
def index():
    #page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(
        # Post.date_posted.desc()).paginate(page=page, per_page=6)
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=582e253204bc4247908077fd638501ff')
    url_2 = ('https://newsapi.org/v2/everything?domains=wsj.com,nytimes.com,espn-cric-info&apiKey=582e253204bc4247908077fd638501ff')
    response = requests.get(url)
    response_2 = requests.get(url_2)
    top_headlines_in = response.json()
    top_headlines_all = response_2.json()
    posts_in = top_headlines_in
    posts_all = top_headlines_all
    x = datetime.datetime.now()
    today_date = x.strftime("%d %b %Y")
    return render_template('index.html', posts_in=posts_in, posts_all=posts_all, title='Home', today_date=today_date)


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/search')
def search():
    return render_template('search.html', title='search')

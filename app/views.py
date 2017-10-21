from flask import render_template
from app import app
from .requests import get_source

@app.route('/')
def index():
    '''
    function that returns the index page
    '''

    # getting source categories
    general_news = get_source('general')
    business_news = get_source('business')
    entertainment_news = get_source('entertainment')
    gaming_news = get_source('gaming')
    music_news = get_source('music')
    politics_news = get_source('politics')
    sports_news = get_source('sport')
    technology_news = get_source('technology')
    

    title = 'News from your Favorite Sources'
    return render_template('index.html', title = title, general = general_news, business = business_news, entertainment = entertainment_news, gaming = gaming_news,
music = music_news, politics = politics_news, sport = sports_news, technology = technology_news)


@app.route('/source/<source_id>')
def source(source_id):
    '''
    returns source with it's articles
    '''
    return render_template('source.html', id = source_id)

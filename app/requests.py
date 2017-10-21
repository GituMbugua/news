from app import app
import urllib.request, json
from .models import source
from .models import article

Source = source.Source
Article = article.Article

# get api key
api_key = app.config['NEWS_API_KEY']

# get base urls
source_base_url = app.config["NEWS_SOURCE_BASE_URL"]
article_base_url = app.config["NEWS_ARTICLE_API_BASE_URL"]

def get_sources(category):
    '''
    function to get the json response to the url request
    '''
    get_sources_url = source_base_url.format(category)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(sources_list):
    sources_results = []
    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')

        sources_object = Source(id, name, description, url, category)
        sources_results.append(sources_object)

    return sources_results

def get_articles(id):
    get_articles_details_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response:
            author = articles_details_response.get('author')
            title = articles_details_response.get('title')
            description = articles_details_response.get('descrition')
            url = articles_details_response.get('url')
            image_url = articles_details_response.get('image_url')
            publish_time = articles_details_response.get('publish_time')

            articles_object = Article(author, title, description, url, image_url, publish_time)

    return articles_object
            
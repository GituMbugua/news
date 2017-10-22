import urllib.request, json
from .models import Source, Article

# get api key
api_key = None

# get base urls
source_base_url = None
article_base_url = None

def configure_requests(app):
    global api_key, source_base_url, article_base_url
    
    api_key = app.config['NEWS_API_KEY']
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
    '''
    function to get json response from url
    '''
    get_articles_details_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_results = None

        if articles_details_response['articles']:
            article_results_list = articles_details_response['articles']
            articles_results = process_articles(article_results_list)
    
    return articles_results

def process_articles(articles_list):
    article_results = []
    for item in articles_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('urlToImage')
        publish_time = item.get('publishedAt')

        articles_object = Article(author, title, description, url, image_url, publish_time)
        article_results.append(articles_object)

    return article_results
            
from app import app
import urllib.request, json
from .models import source

Source = source.Source

# get api key
api_key = app.config['NEWS_API_KEY']

# get base urls
source_base_url = app.config["NEWS_SOURCE_BASE_URL"]
# article_base_url = app.config["NEWS_ARTICLE_API_BASE_URL"]

def get_source(category):
    '''
    function to get the json response to the url request
    '''
    get_source_url = source_base_url.format(category)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None
        
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    source_results = []
    for item in source_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')

        source_object = Source(id, name, description, url, category)
        source_results.append(source_object)

    return source_results
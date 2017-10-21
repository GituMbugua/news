# import os

class Config:
    NEWS_SOURCE_BASE_URL = 'https://newsapi.org/v1/sources?category={}&language=en'
    # NEWS_ARTICLE_API_BASE_URL = 'https://newsapi.org/v1/articles?source={}&apiKey={}
    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # NEWS_API_KEY='3af9695e2c9a47a0827f52a1b4badb83'
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
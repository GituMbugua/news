import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    testing the behaviour of the article class
    '''

    def setUp(self):
        '''
        runs before every test
        '''
        self.new_article = Article("Gitu Mbugua", "Testing Article Class", "This text represents an article...",
        "http://dummylink.com/more-link", "https://dummylink.com/image.jpg", "2017-10-22T09:00:32Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

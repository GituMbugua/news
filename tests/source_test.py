import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    testing the behaviour of the source class
    '''

    def setUp(self):
        '''
        runs before every test
        '''
        self.new_source = Source("mtv-news", "MTV News", "All the latest news from the world of music and entertainment.", "http://www.mtv.co.uk/news", "music")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

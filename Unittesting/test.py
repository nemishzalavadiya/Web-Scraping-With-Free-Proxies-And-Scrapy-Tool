import unittest
from goog.spiders.GoogCompetitor import GoogNameJson

class check_googcompetitor(unittest.TestCase):

    def __init__(self):
        self.googCompetitor = GoogNameJson()

    def check_symbol(self):
        self.assert_()
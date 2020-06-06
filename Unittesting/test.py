import unittest
from Utilities.symbolUtil import SymbolUtil
from Utilities.XmlUtil import XmlProxyUtil,XmlScrapeUtil

# from root directory
# run cmd : python -m unittest Unittesting.test.CheckGoogCompetitor.check_symbol

class CheckGoogCompetitor(unittest.TestCase):

    # indeed tests for project
    def check_symbol(self):
        self.assertEqual(SymbolUtil.get_symbol_from_url("http://dummy/running/work/goog/overview"), "GCompetent")

    def check_proxy_url(self):
        self.assertEqual(XmlProxyUtil().get_proxy_url(),"https://free-proxy-list.net/")

    def check_scrape_url(self):
        self.assertEqual(XmlScrapeUtil.get_scraping_url(),("https://www.barchart.com/stocks/quotes/","/overview"))

if __name__ == '__main__':
    unittest.main()

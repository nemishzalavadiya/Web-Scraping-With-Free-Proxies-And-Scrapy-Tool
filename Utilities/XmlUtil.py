# noinspection PyUnresolvedReferences
from xml.dom.minidom import parse
# noinspection PyUnresolvedReferences
import xml.dom.minidom
import sys
class XmlScrapeUtil:

    def __init__(self):
        self.DOMTree = xml.dom.minidom.parse("../ConfigurationXML/scrapeurl.xml")
        self.collection = self.DOMTree.documentElement

    def get_scraping_url(self):
        self.url_scrap = self.collection.getElementsByTagName("url")
        for url in self.url_scrap[:1]:
            self.pre = url.getElementsByTagName("pre")[0].childNodes[0].data
            self.end = url.getElementsByTagName("end")[0].childNodes[0].data
        return (self.pre[1:-1] , self.end[1:-1])

class XmlProxyUtil:

    def __init__(self):
        self.DOMTree = xml.dom.minidom.parse("../ConfigurationXML/proxyurl.xml")
        self.collection = self.DOMTree.documentElement

    def get_proxy_url(self):
        self.url_scrap = self.collection.getElementsByTagName("url")
        for url in self.url_scrap[:1]:
            if url.hasAttribute("site"):
                self.site = url.getAttribute("site")
        return self.site[1:-1]
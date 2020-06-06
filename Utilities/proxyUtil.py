import requests
from lxml.html import fromstring
from Utilities.XmlUtil import XmlProxyUtil
import sys

class ProxyUtil:

    # here i have used static side to get free ip's to change on each run in cycle
    @staticmethod
    def get_proxies():
        url = XmlProxyUtil().get_proxy_url()
        if url==None:
            sys.exit("No Urls Found In proxyurl.xml file")
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:30]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                # Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies

    # creating free proxies adding to the file
    def create_proxy(self):
        with open('../goog/proxy_list.txt', 'a') as fp:
            for ip in self.get_proxies():
                fp.write("http://" + ip + '\n')
#imports
#here to get parsing i have used lxml
#so, install is : pip install xml
import requests
from lxml.html import fromstring
import scrapy
from finsymbols import symbols

class GoogNameJson(scrapy.Spider):
    ''' Class to scrape the GOOG Competitors '''
    name = "GOOGCompetitor"
    pre_url = 'https://www.barchart.com/stocks/quotes/'
    end_url = '/overview'
    start_urls = [   
    ]

    def get_proxies(self):
        ''' here i have used static side to get free ip's to change on each run in cycle '''
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text)
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:30]:
            if i.xpath('.//td[7][contains(text(),"yes")]'):
                #Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)
        return proxies

    #generate Symbol
    def get_symbols(self):
        return symbols.get_sp500_symbols()

    #creating free proxys
    def createProxy(self):
        with open('./list.txt','a') as fp:
            for ip in self.get_proxies():
                fp.write("http://"+ip+'\n')


    #find out Symbols from finsymbols
    def __init__(self):
        self.createProxy()
        self.sp = self.get_symbols()
        for ever in self.sp:
            self.start_urls.append(self.pre_url+ever['symbol'].strip()+self.end_url)

    #create symbol name from url
    def get_symbol_from_url(self,url):
        return url.split('/')[5]

    #parser to get data and store it as a json File
    def parse(self,response):
        symbol = self.get_symbol_from_url(response.url)
        location_of_Name = "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/h1/span[1]/text()"
        yield {
            'Symbol':symbol,
            "Name":response.xpath(location_of_Name).extract_first(),
        }
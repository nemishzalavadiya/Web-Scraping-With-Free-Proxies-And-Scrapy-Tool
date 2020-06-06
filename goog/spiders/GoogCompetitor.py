# imports
import scrapy
import sys
from Utilities.proxyUtil import ProxyUtil
from Utilities.symbolUtil import SymbolUtil
from Utilities.XmlUtil import XmlScrapeUtil


class GoogNameJson(scrapy.Spider):
    ''' Class to scrape the GOOG Competitors '''
    name = "GOOGCompetitor"
    start_urls = [
    ]

    # find out Symbols from finsymbols
    def __init__(self, path=" "):

        ProxyUtil().create_proxy()  # to create proxy file
        self.pre_url, self.end_url = XmlScrapeUtil().get_scraping_url()
        if self.pre_url is None or self.end_url is None:
            sys.exit("No Url Found in scrapeurl.xml file to scrape")
        self.prepare_start_urls(path)  # create urls paths
        return

    def prepare_start_urls(self, path):
        if path == " ":
            self.sp = SymbolUtil.get_symbols()
            for ever in self.sp:
                self.start_urls.append(self.pre_url + ever["symbol"].strip() + self.end_url)
        else:
            try:
                with open("../" + path, 'r') as fp:
                    syllable = fp.read()
                    self.sp = [symbol_.strip() for symbol_ in syllable.split(',')]
                    for ever in self.sp:
                        self.start_urls.append(self.pre_url + ever + self.end_url)
            except Exception as e:
                sys.exit("file operation failed " + str(e))

    # parser to get data and store it as a json File
    def parse(self, response):
        symbol = SymbolUtil.get_symbol_from_url(response.url)
        try:
            location_of_Name = "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div[1]/h1/span[1]/text()"
            yield {
                'Symbol': symbol,
                "Name": response.xpath(location_of_Name).extract_first(),
            }
        except Exception as e:
            print("connection failed with site for provided symbol " + symbol)

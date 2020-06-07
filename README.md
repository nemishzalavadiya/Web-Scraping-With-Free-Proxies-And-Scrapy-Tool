# Web_Scraping_Using_Proxies_And_Scrapy-Tool
## Click and Use  `Run_Me.sh` file
Scrapy project with Free Proxies and also by obeying robot.txt file rules of website
### https://www.barchart.com/robots.txt
Sitemap: https://www.barchart.com/sitemap.xml

 - User-agent: `Disallow: /proxies/`

 - User-agent: proximic `Disallow: /`

 - User-agent: msnbot `Crawl-delay: 3`

> Approch

      <p>&nbsp&nbsp&nbsp Here, In this approch, I have used complete transparancy by getting every line of json file with different request by changing ip address. Which by the way i got from free-proxies site. So, It's going to take time because some proxies are invalide. It's very much secure because of scrapy's inbuilt support. which is choice of major web scraper because of simplicity and efficiency.</p>
      <p>&nbsp&nbsp becuase of this approch, It's gonna take time to load all the data from the site or depend on the file user have provided to fetch the data. less symbols in file less request will be generated.</p>

> Why Scrapy?

### Scrapy is a very efficient and handy tool for web scraping purpose. I have used it here in this project where what i did is,
 - Created genspider using scrapy startproject cmd which gives supporting environment for data extraction which is pipeline support for
    requests.
 - efficient middlewares to handle proxes, use other api services while scraping et cetera.
 - scrapy also provides support for various operations number of proxies per requests, Download_middle directely etc. in setting.py
   file.
   
### One of my favorite in Scrapy is scrapy.Spider class,
 - scrapy has a very userful scrapy.Spider class which provides a essential code for scraping which we can utilize as a super class and
   take advantage by saving lots of time and most important is our time.

### my scraping code is written in Spider/GOOGCompetitor.py file

#### I have used free proxies from https://free-proxy-list.net/.
      Here is a screenshot of received proxies,
![proxy list](https://github.com/nemishzalavadiya/Web_Scraping_Using_Proxies_And_Scrapy/blob/master/Screenshot/proxy_list.PNG)
      
#### Output get from this scraping is available in json file inside goog folder with provided name in a script file.
      Here is a screenshot of the sample json file,
![goog list of competitor](https://github.com/nemishzalavadiya/Web_Scraping_Using_Proxies_And_Scrapy/blob/master/Screenshot/goog_list_json.PNG)
      
#### Here I have created Utility Class, Unittesting Class, ConfigurationXml Files etc. to manage organization of code as well as make it look modularized.
 
 - Utility Class
   - ProxyUtility
   - SymbolUtility
   - XmlUtility
 - Unittesting
   - test
 - goog
   - spiders
    - GoogCompetitor ( Functional Requirements performed here )
   - setting.py and other util classes of scrapy      


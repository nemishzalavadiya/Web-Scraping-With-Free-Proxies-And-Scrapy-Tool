# Web_Scraping_Using_Proxies_And_Scrapy
## Click and Use --> run_me.sh file
Scrapy project with Free Proxies and also by obeying robot.txt file rules of website
### https://www.barchart.com/robots.txt
Sitemap: https://www.barchart.com/sitemap.xml

 - User-agent: * ->
   Disallow: /proxies/

 - User-agent: proximic ->
   Disallow: /

 - User-agent: msnbot ->
   Crawl-delay: 3

### Scrapy is a very efficient and handy tool for web scraping purpose. I have used it here in this project where what i did is,
 - Created genspider using scrapy startproject cmd which gives supporting environment for data extraction which is pipeline support for
    requests.
 - efficient middlewares to handle proxes, use other api services while scraping et cetera.
 - scrapy also provides support for various operations number of proxies per requests, Download_middle directely etc. in setting.py
   file.
   
### One of my favorite in Scrapy is scrapy.Spider class,
 - scrapy has a very userful scrapy.Spider class which provides a essential code for scraping which we can utilize as a super class and
   take advantage by saving lots of time and most important is our time.

### my scraping code is written in GOOGCompetitor.py file

#### I have used free proxies from https://free-proxy-list.net/.
      Here is a screenshot of received proxies,
![proxy list](https://github.com/nemishzalavadiya/Web_Scraping_Using_Proxies_And_Scrapy/blob/master/Screenshot/proxy_list.PNG)
      
      
      
      
      


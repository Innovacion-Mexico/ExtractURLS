import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search


def get_urls(tag, n, language):
    urls = [url for url in search(tag, stop=n, lang=language)][:n]
    return urls

def get_urls(tag, n, language, xContry):  # filtering by country
    urls = [url for url in search(tag, stop=n, lang=language, country=xContry, tpe= 'nws')][:n]
    return urls

def get_urls(tag, n, language, xContry, xTPE):  # filtering by country, and type of nws stand for news
    urls = [url for url in search(tag, stop=n, lang=language, country=xContry, tpe= xTPE)][:n]
    return urls

#https://stenevang.wordpress.com/2013/02/22/google-advanced-power-search-url-request-parameters/
# filtering by country, and type of nws stand for news
def get_urls(tag, n, language, xContry, dateBegin, dateEnd):  
	print('here we go!')
	urls = [url for url in search(tag, stop=n, lang=language, country=xContry, tbs='cdr:1,cd_min:3/2/2020,cd_max:4/2/2020')][:n]
	#urls = [url for url in search(tag, stop=n, lang=language, country=xContry, tbs='qdr:d')][:n]
	return urls



def parse(self, response):        
	links = LxmlLinkExtractor(allow=()).extract_links(response)
	links = [str(link.url) for link in links]
	links.append(str(response.url))    
	for link in links:
		yield scrapy.Request(url=link, callback=self.parse_link) 


def main():
	googleURL=get_urls('Covid19',15,'es', 'Mexico','3/3/2020','31/3/2020' )
	print("\n")
	print(googleURL)

if __name__ == "__main__":
    main()
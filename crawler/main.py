# coding=UTF-8

print('crawler begining!')
fundCompanyBaseUrl='http://fund.eastmoney.com'

from urllib import request
from bs4 import BeautifulSoup 
from bs4.element import Tag 
import logging
 
from FundCompanyListCrawler import *
from FundCompanyCrawler import *

import logging
import os
from logging import handlers

from utils.LoggingConfig import _getLogger
import time
from FundCrawler import FundCrawler
log=_getLogger()
log.error('ddddd')


#fundCompanyListCrawler =FundCompanyListCrawler()
#fundCompanyListCrawler.beginJob()
fundCompanylist=FundCompanyListCrawler.getListFromFile()
FundCrawler.getAndSaveFundPageHtml('010753','招商招旭纯债D')
 
if(__name__=="__main__"):
 #  exit(0)
   pass

for item in fundCompanylist:
    pass
    url=fundCompanyBaseUrl+item['href']
    name=item['name']
    url=fundCompanyBaseUrl+'/Company/80036782.html'
    name='招商'
    #FundCompanyCrawler.getAndSaveDetailHtml(url,name)
    time.sleep(0.2)
    FundCompanyCrawler.parseFromHtmlFile(name);
    break;



### 解析基金公司详细信息
def parseFundCompanyDetailHtmlPage(url,name):
    fullFundCompanyDetailUrl=fundCompanyBaseUrl+url
    print(fullFundCompanyDetailUrl)
    with request.urlopen(fullFundCompanyDetailUrl) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        
        print('Data:', data.decode('utf-8'))

        print(fullFundCompanyDetailUrl)

    return





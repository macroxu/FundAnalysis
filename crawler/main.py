# coding=UTF-8

print('crawler begining!')
fundCompanyBaseUrl='http://fund.eastmoney.com'

from urllib import request
from bs4 import BeautifulSoup 
from bs4.element import Tag 
import logging
 
from FundCompanyListCrawler import *

import logging
import os
from logging import handlers

from utils.LoggingConfig import _getLogger
 
log=_getLogger()
log.error('ddddd')


fundCompanyListCrawler =FundCompanyListCrawler()
#fundCompanyListCrawler.beginJob()

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





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

from analysis.FundCompanyAnalysis import *

log=_getLogger()
log.error('ddddd')

fundCompanyList=FundCompanyListCrawler.getListFromFile()

FundCompanyAnalysis.getMaxBuildFundCompanyList()

#df=pd.DataFrame(FundDataCompanyList)
 
if(__name__=="__main__"):
   exit(0)
   pass

for fundCompany in fundCompanyList:
    fundCompanyName=fundCompany['name']
    print('开始处理：'+fundCompanyName)
    fundList=FundCompanyCrawler.getFundListByCompanyFile(fundCompanyName)
    FundCrawler.beginDownLoadHtmlJob(fundList)
    FundCrawler.beginParseHtmlJob(fundList)

 
#FundCrawler.parseFromHtmlFile('007897','易方达优选多资产三个月持有混合(FOF)C')

if(__name__=="__main__"):
   exit(0)
   pass

#fundCompanyListCrawler =FundCompanyListCrawler()
#fundCompanyListCrawler.beginJob()
fundCompanylist=FundCompanyListCrawler.getListFromFile()
FundCrawler.getAndSaveFundPageHtml('010753','招商招旭纯债D')
 
#测试解析
FundCrawler.parseFromHtmlFile('007897','易方达优选多资产三个月持有混合(FOF)C')


if(__name__=="__main__"):
   exit(0)
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





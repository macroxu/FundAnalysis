from urllib import request
from  utils.FileManager import FileManager
import os
from string import Template
from bs4 import BeautifulSoup
from bs4 import Tag 

fundCompanyBaseUrl='http://fundf10.eastmoney.com/jbgk_'
#基金
class FundCrawler:
    def __init__(self):
        pass
    
    #获取并保存基金Pagehtml
    @staticmethod
    def getAndSaveFundPageHtml(fundCode,fundName):
        url=fundCompanyBaseUrl+fundCode+'.html'
        with request.urlopen(url) as f:
            data=f.read()
            utf8data=data.decode('utf-8')

            #save to file
            FileManager.saveStringSteamToFile('/datas/funds/'+fundName+fundCode+".html",utf8data)
        return

    @staticmethod
    def parseFromHtmlFile(fundCode,fundName):
        #read html File
        filePath='datas/funds/'+fundName+fundCode+".html"
        htmlData=FileManager.readStringSteamToFile(filePath)

        fundInfo={}
        #parse page
        soup= BeautifulSoup(htmlData,"html.parser")

        saveFilePath='datas/funds/'+fundName+fundCode+".html"
        FileManager.saveDicAsJsonToFile(filePath,fundInfo)

        pass

    

# fund company crawlwer
# get and save html to storage,
# parse html and convert to json data, then save it in storage
from urllib import request
from  utils.FileManager import FileManager
import os
from utils.LoggingConfig import _getLogger
from bs4 import BeautifulSoup
from bs4.element import Tag 
from utils.BeautifulSoupParseHelper import BeautifulSoupParseHelper
class FundCompanyCrawler:
    def __init__(self):
        return

    @staticmethod
    def getAndSaveDetailHtml(url,fundName):
        _getLogger().info('begin get['+fundName+']')
        with request.urlopen(url) as f:
            data=f.read()
            utf8data=data.decode('utf-8')
         
            #save to file
            os.makedirs(FileManager.getCurPath()+'/datas',exist_ok=True)
            filename=FileManager.getCurPath()+'/datas/'+fundName+".html"
            with open(filename,'w',encoding='utf-8') as file_obj:
                file_obj.write(utf8data)
        _getLogger().info('finish get['+fundName+']')
        return
    
    @staticmethod
    def parseFromHtmlFile(fundName):
        pass
        filename=FileManager.getCurPath()+'/datas/'+fundName+'.html'
         #读取文件
        utf8Data=''
        with open(filename,'r',encoding='utf8')as fp:
            utf8Data=fp.read();
        
        #定义提取变量
        fundCompany={}
        soup = BeautifulSoup(utf8Data, 'html.parser')
        
        #name
        BeautifulSoupParseHelper.parseSingleStr(soup,'.ttjj-panel-main-title',fundCompany,'companyName')
        #enName
        BeautifulSoupParseHelper.parseSingleStr(soup,'.ttjj-panel-sub-title',fundCompany,'companyEnName')
         
        #联系方式

        attrsName=('officeAddress', 'generalManager', 'website', 'customerServiceHotline')
        BeautifulSoupParseHelper.parseArrayStr(soup,'.firm-contact p label',fundCompany,attrsName)
               

        #基金信息
        fundInfoTag=soup.select('.fund-info ul li label.grey' )
        print(fundInfoTag)
       
        fundCompany['managementScale']=fundInfoTag[0].string
        fundCompany['fundNo']=fundInfoTag[1].a.string
        fundCompany['fundManagerNo']=fundInfoTag[2].a.string
        fundCompany['createdDate']=fundInfoTag[3].string
        fundCompany['assetType']=fundInfoTag[4].string
        print(fundCompany)

        
        
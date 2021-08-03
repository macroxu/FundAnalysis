# fund company crawlwer
# get and save html to storage,
# parse html and convert to json data, then save it in storage
from urllib import request
from  utils.FileManager import FileManager
import os
from utils.LoggingConfig import _getLogger
from bs4 import BeautifulSoup
from bs4.element import Tag 
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
        companyNameTag = soup.find(attrs={'class':'ttjj-panel-main-title'})
        fundCompany['companyName']=companyNameTag.string

        #enName
        companyNameEnTag=soup.select_one('.ttjj-panel-sub-title')
        fundCompany['companyEnName']=companyNameEnTag.string

        #联系方式
        firmContactTag=soup.select('.firm-contact p label' )
        fundCompany['officeAddress']=firmContactTag[0].string
        fundCompany['generalManager']=firmContactTag[1].string         
        fundCompany['website']=firmContactTag[2].string         
        fundCompany['customerServiceHotline']=firmContactTag[3].string         

        #基金信息
        fundInfoTag=soup.select('.fund-info ul li' )
        fundCompany['managementScale']=fundInfoTag[0].label.string
         

        print(fundCompany)

        
        
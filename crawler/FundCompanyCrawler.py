# fund company crawlwer
# get and save html to storage,
# parse html and convert to json data, then save it in storage
from urllib import request
from  utils.FileManager import FileManager
import os
import json
from utils.LoggingConfig import _getLogger
from bs4 import BeautifulSoup
from bs4.element import Tag 
from utils.BeautifulSoupParseHelper import BeautifulSoupParseHelper
import pathlib


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
            os.makedirs(FileManager.getCurPath()+'/datas/fundcompanyhtml',exist_ok=True)
            filename=FileManager.getCurPath()+'/datas/fundcompanyhtml/'+fundName+".html"
            with open(filename,'w',encoding='utf-8') as file_obj:
                file_obj.write(utf8data)
        _getLogger().info('finish get['+fundName+']')
        return
    
    @staticmethod
    def parseFromHtmlFile(fundCompanyName):
        pass
        filename=FileManager.getCurPath()+'/datas/fundcompanyhtml/'+fundCompanyName+'.html'
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

        #解析开放式基金列表
        fundOutlineList=soup.select('#kfsFundNetWrap tbody tr td.fund-name-code')
        print(fundOutlineList)
        kfsFundList=[] #开放式基金列表
        if fundOutlineList!=None:
            for td in fundOutlineList:
                fundName=td.select('.name')
                fundValue=td.select('.code')
                fundNameCode={'name':fundName[0].string,'code':fundValue[0].string}
                kfsFundList.append(fundNameCode)
        
        fundCompany['kfsFundList']=kfsFundList

        #解析货币/理财型基金列表
        HBLCFundTDList=soup.select('#HBLCFundNetCon tbody tr td.fund-name-code')
        HBLCFundList=[]
        if HBLCFundTDList!=None:
            for td in HBLCFundTDList:
                fundName=td.select('.name')
                fundValue=td.select('.code')
                fundNameCode={'name':fundName[0].string,'code':fundValue[0].string}
                HBLCFundList.append(fundNameCode)
        fundCompany['HBLCFundList']=HBLCFundList


        #解析场内基金
        CNFundNetTDList=soup.select('#CNFundNetCon tbody tr td.fund-name-code')
        CNFundList=[]
        if CNFundNetTDList!=None:
            for td in CNFundNetTDList:
                fundName=td.select('.name')
                fundValue=td.select('.code')
                fundNameCode={'name':fundName[0].string,'code':fundValue[0].string}
                CNFundList.append(fundNameCode)
        fundCompany['CNFundList']=CNFundList

        #将数据保存到Datas/fundcompany文件夹中
        listFileName=FileManager.checkAndCreateDir(FileManager.getCurPath());
        os.makedirs(listFileName+'/datas/fundcompany',exist_ok=True)
        filename=listFileName+'/datas/fundcompany/'+fundCompanyName +'.json'
        with open(filename,'w',encoding='utf-8') as file_obj:
            json.dump(fundCompany,file_obj,ensure_ascii=False)

        return

        print(fundCompany)

    @staticmethod
    def getFundCompanyInfoByCompanyFile(funcCompanyName):
        #根据fundName 读取文件
        filename=FileManager.getCurPath()+'/datas/fundcompany/'+funcCompanyName+'.json'
        path = pathlib.Path(filename)
        if not path.exists():
            return 
        
        #读取文件
        json_data=None
        with open(filename,'r',encoding='utf8')as fp:
            json_data = json.load(fp)
        
        
        return json_data

        

    @staticmethod
    def getFundListByCompanyFile(fundCompanyName):
    
        #读取文件
        json_data=FundCompanyCrawler.getFundCompanyInfoByCompanyFile()
        
        #将三个类型的基金列表进行合并
        kfsFundList=json_data['kfsFundList']
        HBLCFundList=json_data['HBLCFundList']
        CNFundList=json_data['CNFundList']
        fundlist=[]
        fundlist.extend(kfsFundList)
        fundlist.extend(HBLCFundList)
        fundlist.extend(CNFundList)

        return fundlist


        
        
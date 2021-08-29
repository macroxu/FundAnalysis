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
            FileManager.saveStringSteamToFile('/datas/fundhtml/'+fundName+fundCode+".html",utf8data)
        return

    @staticmethod
    def parseFromHtmlFile(fundCode,fundName):
        #read html File
        filePath='datas/fundhtml/'+fundName+fundCode+".html"
        htmlData=FileManager.readStringSteamToFile(filePath)
        #print(htmlData)
        fundInfo={}
        #parse page
        soup= BeautifulSoup(htmlData,"html.parser")
    
        #table解析部分
        attrNames=['fundFullName','fundAbbreviation','fundCode','fundType','issueDate','dateOfEstablishmentScale'
                    ,'assetScale','assetManager','fundCustodian','fundManager','setupToPayDividends','managementRate'
                    ,'escrowRate','salesServiceRate','maximumSubscriptionRate','maximumSubscriptionFeeRate','maximumRedemptionRate',
                    'performanceBenchmark','trackingSubject']
        th_titles=['基金全称','基金简称','基金代码','基金类型','发行日期','成立日期/规模','资产规模','基金管理人'
                    ,'基金托管人','基金经理人','成立来分红','管理费率','托管费率','销售服务费率'
                    ,'最高认购费率','最高赎回费率','最高赎回费率','业绩比较基准','跟踪标的']
        txt_values=[]
        for title in th_titles:
            th_title=soup.find('th',text=title)
            td_value=th_title.next_sibling
            
            valueOfTitle=td_value.text
            txt_values.append(valueOfTitle)

        attrs=dict(zip(attrNames,txt_values))
        
        fundInfo.update(attrs)
        

        #投资目标 投资理念 投资范围 投资策略 分红政策 风险收益特征
        divList=soup.select('.box p')
        #投资目标
        investTitles=['investObject','investPhilosophy','investScope','investStrategy','dividendPolicy','Risk-returnCharacteristics']
        investObject=divList[0].string

        listInvest=list([pTag.string for pTag in divList])
        dictInvest=dict(zip(investTitles,listInvest))
        
        fundInfo.update(dictInvest)
        
        #保存到文件中
        for key,value in fundInfo.items():
            print(key+':'+value)

        saveFilePath='datas/funds/'+fundName+fundCode+".json"
        FileManager.saveDicAsJsonToFile(saveFilePath,fundInfo)

        pass

    

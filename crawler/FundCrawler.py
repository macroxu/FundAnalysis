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

        #获取table 的tr部分
        trList=soup.select('.info tr')
         
        fundDic={} 
        
        for tr in trList:
            datas=[]
            for index, child in enumerate(tr.children):
                datas.append(child.string)
            #转化成dic
            dictTR=dict(zip(datas[0::2],datas[1::2]))   

            for key,value in dictTR.items():
                value=value if value else ''
                #print(key+'/'+value)
                fundDic[key]=value
            pass
            
        print(fundDic)
        
        #投资目标 投资理念 投资范围 投资策略 分红政策 风险收益特征
        divList=soup.select('.box p')
        #投资目标
        investTitles=['investObject','investPhilosophy','investScope','investStrategy','dividendPolicy','Risk-returnCharacteristics']
        investObject=divList[0].string

        listInvest=list([pTag.string for pTag in divList])
        dictInvest=dict(zip(investTitles,listInvest))

        print(dictInvest)

        saveFilePath='datas/funds/'+fundName+fundCode+".json"
        FileManager.saveDicAsJsonToFile(saveFilePath,fundInfo)

        pass

    

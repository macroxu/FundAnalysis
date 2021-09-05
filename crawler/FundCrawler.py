from urllib import request
from  utils.FileManager import FileManager
import os
from string import Template
from bs4 import BeautifulSoup
from bs4 import Tag 
import time


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
        boxList=soup.select('.box')
        #投资目标
        investTitles=['investObject','investPhilosophy','investScope','investStrategy','dividendPolicy','Risk-returnCharacteristics']
        investValues=[]
        #重新解析,在box 里面 存在多个p 

        firstBox=True
        for box in boxList:
            if firstBox:
                pass
                firstBox=False
            else:
                #读取数据
                pass
                pInBox=box.select('p')
                investValue=''
                for p in pInBox:
                    if(len(investValue)>0):
                        investValue+='\n'
                    if(p.string):
                        investValue+=p.string
                
                investValues.append(investValue)
                

        dictInvest=dict(zip(investTitles,investValues))
        print(dictInvest)
        fundInfo.update(dictInvest)
        
        #保存到文件中
        for key,value in fundInfo.items():
            print(key+':'+value)

        saveFilePath='datas/funds/'+fundName+fundCode+".json"
        FileManager.saveDicAsJsonToFile(saveFilePath,fundInfo)

        pass

    
        ### 开始执行任务
    @staticmethod
    def beginDownLoadHtmlJob(fundList):
        #循环
        for fund in fundList:
            name=fund['name'].replace('/','_') #特殊字符 A/B 可能引起路径问题 A_B
            code=fund['code']
            print(name+":"+code+':开始爬取html')

            #查找文件是否存在，存在的话不用下载
            filePath=FileManager.getCurPath()+'/datas/fundhtml/'+name+code+".html"
            if not os.path.exists(filePath):
                FundCrawler.getAndSaveFundPageHtml(code,name)
                time.sleep(0.3)
        #
        pass
    
    @staticmethod
    def beginParseHtmlJob(fundList):
        for fund in fundList:
            name=fund['name'].replace('/','_') #特殊字符 A/B 可能引起路径问题 A_B
            code=fund['code'] 
            print(name+":"+code+":开始解析html")

            #查看解析文件的文件是否存在，存在不解析
            filePath=FileManager.getCurPath()+'/datas/funds/'+name+code+".json"
            if not os.path.exists(filePath):
                print('找不到'+filePath)
                FundCrawler.parseFromHtmlFile(code,name)
                time.sleep(0.3)
        
        pass



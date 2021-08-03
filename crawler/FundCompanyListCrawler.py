# the crawler 
#      get and parse  the page of fund company list
# parse and save company name  and detail url 
from urllib import request
from bs4 import BeautifulSoup 
from bs4.element import Tag 
import json
import os
from  utils.FileManager import FileManager
import pathlib
class FundCompanyListCrawler:
    fundCompanyList='http://fund.eastmoney.com/Company/default.html'

    def __init__(self):
         return

    
    def parseFundCompanyListHtmlPage(self,contentStr):
        """by contentStr,parse data,build data as json ,and save into file for next step
            :param contentStr: html Str

        """
        soup = BeautifulSoup(contentStr, 'html.parser')

        items = soup.find(attrs={'class':'sencond-block'}).children

        #创建数组,保存挖掘的fund company 列表
        fundCompanySummaryList=[]

        for item in items:
            #print(item)
            if(type(item)==Tag):
                print(item)
                #创建对象
                if(item.name=="a"):
                    href=item.attrs['href']
                    companyName=item.string
                    #parseFundCompanyDetailHtmlPage(href,companyName)
                    fundCompanySummary={

                    }
                    fundCompanySummary['href']=href
                    fundCompanySummary['name']=companyName
                    fundCompanySummaryList.append(fundCompanySummary)
                    

        #将json数据保存到文件中
        listFileName=FileManager.checkAndCreateDir(FileManager.getCurPath());

        print(fundCompanySummaryList)
         
        os.makedirs(listFileName+'/datas',exist_ok=True)
        filename=listFileName+'/datas/fundcompanylist.json'
        with open(filename,'w',encoding='utf-8') as file_obj:
            json.dump(fundCompanySummaryList,file_obj,ensure_ascii=False)

        return

    ### 开始执行任务
    def beginJob(self):
        print('begin')
        ###获取基金公司列表
        with request.urlopen(self.fundCompanyList) as f:
            data = f.read()
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', data.decode('utf-8'))
            self.parseFundCompanyListHtmlPage(data.decode('utf-8'))
        return
 
    #从文件中获取json对象,并将json对话转化成dic
    @staticmethod
    def getListFromFile():
        #判断 文件是否存在
        filename=FileManager.getCurPath()+'/datas/fundcompanylist.json'
        path = pathlib.Path(filename)
        if not path.exists():
            return 
        
        #读取文件
        with open(filename,'r',encoding='utf8')as fp:
            json_data = json.load(fp)
            
            return json_data
        pass





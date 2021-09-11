
from FundCompanyListCrawler import *
import pandas as pd

#定义基金公司分析数据
class FundCompanyAnalysis:
    def __init__(self):
        return

    @staticmethod
    def getMaxMarketValueList():
        fundCompanyInfoList=FundCompanyListCrawler.getFundCompanyDataList()
        #print(fundCompanyInfoList)

        df=pd.DataFrame(fundCompanyInfoList)

        #获取基金公司名称 和份额
        df_data=df[['companyName','managementScale']]
        print(df_data)

        #将managementScale 字符串转化成数字
        managementScaleList=df['managementScale'].tolist()
        newManagementScaleList=[]
        print(managementScaleList)
        for item in managementScaleList:
            if item=='---':
                item='0.0亿元'
            #除去亿元两个字
            item=item.replace('亿元','')
            
            newManagementScaleList.append(item)
        
        

        print(newManagementScaleList)


        seris=df['fundNo_number']=df['fundNo']
        seris.map(lambda x:100)      
        print(type(df['fundNo_number']))

        print(df.info())
        #排序
        sortDf=df.sort_values('fundNo_number',ascending=False)


        print(sortDf.head(10)['fundNo_number'])
        #print(df)                


        pass



from FundCompanyListCrawler import *
import pandas as pd

#定义基金公司分析数据
class FundCompanyAnalysis:
    def __init__(self):
        return

    #获取成立最久的10家基金公司
    @staticmethod
    def getMaxBuildFundCompanyList():
        fundCompanyInfoList=FundCompanyListCrawler.getFundCompanyDataList()
        df=pd.DataFrame(fundCompanyInfoList)
        print(df.info()) 

        #获取基金公司名称 和份额
        df_data=df[['companyName','createdDate']]
        print(df_data)
        
        df_data_sort=df_data.sort_values('createdDate',ascending=True)
        print(df_data_sort)

        #取前10基金公司
        top10data=df_data_sort.head(10)
        print(top10data)

        top10data.to_csv('fundCompanyBuildOldList.csv',index=False)

        pass

    





    @staticmethod
    def getMaxMarketValueList():
        fundCompanyInfoList=FundCompanyListCrawler.getFundCompanyDataList()
        #print(fundCompanyInfoList)

        df=pd.DataFrame(fundCompanyInfoList)
        print(df.info()) 

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
            #字符串转化成float
            item=float(item)

            newManagementScaleList.append(item)

        #添加新的一列数据
        df_data['managementScale']=newManagementScaleList

        #按照资产规模，降序排列
        df_data_sort=df_data.sort_values('managementScale',ascending=False)

        print(df_data_sort)
        #取10行数据
        top10data=df_data_sort.head(10)
        
        #重新排序升序
        top10data_asc=top10data.sort_values('managementScale',ascending=True)

        #将两列数据导出来
        companyNameList=top10data_asc['companyName'].values.tolist()

        managementScaleList=top10data_asc['managementScale'].values.tolist()

        print(companyNameList)
        print(managementScaleList)



        seris=df['fundNo_number']=df['fundNo']
        seris.map(lambda x:100)      
        #print(type(df['fundNo_number']))

        #print(df.info())
        #排序
        sortDf=df.sort_values('fundNo_number',ascending=False)


        #print(sortDf.head(10)['fundNo_number'])
        #print(df)                


        pass


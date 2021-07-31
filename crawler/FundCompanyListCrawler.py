# the crawler 
#      get and parse  the page of fund company list
# parse and save company name  and detail url 
from urllib import request
from bs4 import BeautifulSoup 
from bs4.element import Tag 

 
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

        for item in items:
            #print(item)
            if(type(item)==Tag):
                print(item)
                if(item.name=="a"):
                    href=item.attrs['href']
                    companyName=item.string
                    #parseFundCompanyDetailHtmlPage(href,companyName)
                    return;

        """
        href=item.attrs['href']
        content=item.string
        print(content+href)
        """
        return

    ### 开始执行任务
    def beginJob(self):
        ###获取基金公司列表
        with request.urlopen(self.fundCompanyList) as f:
            data = f.read()
            print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                print('%s: %s' % (k, v))
            print('Data:', data.decode('utf-8'))
            self.parseFundCompanyListHtmlPage(data.decode('utf-8'))
        return
 

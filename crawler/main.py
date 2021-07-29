print('crawler begining!')

fundCompanyList='http://fund.eastmoney.com/Company/default.html'
fundCompanyBaseUrl='http://fund.eastmoney.com'

from urllib import request
from bs4 import BeautifulSoup 
from bs4.element import Tag 



###解析基金公司详细信息
def parseFundCompanyDetailHtmlPage(url,name):
    fullFundCompanyDetailUrl=fundCompanyBaseUrl+url
    print(fullFundCompanyDetailUrl)
    with request.urlopen(fullFundCompanyDetailUrl) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        
        print('Data:', data.decode('utf-8'))

        print(fullFundCompanyDetailUrl)

    return



###解析基金公司列表信息
def parseFundCompanyListHtmlPage( str ):
    #print (str)
    soup = BeautifulSoup(str, 'html.parser')

    items = soup.find(attrs={'class':'sencond-block'}).children

    for item in items:
        #print(item)
        if(type(item)==Tag):
            print(item)
            if(item.name=="a"):
                href=item.attrs['href']
                companyName=item.string
                parseFundCompanyDetailHtmlPage(href,companyName)
                return;

        """
        href=item.attrs['href']
        content=item.string
        print(content+href)
        """
    return


###获取基金公司列表
with request.urlopen(fundCompanyList) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
    parseFundCompanyListHtmlPage(data.decode('utf-8'))


print('crawler begining!')

fundCompanyList='http://fund.eastmoney.com/Company/default.html'

from urllib import request
from bs4 import BeautifulSoup 
from bs4.element import Tag 

###解析
def parseHtmlPage( str ):
    #print (str)
    soup = BeautifulSoup(str, 'html.parser')

    items = soup.find(attrs={'class':'sencond-block'}).children

    for item in items:
        #print(item)
        if(type(item)==Tag):
            print(item)
            if(item.name=="a"):
                print(item.attrs['href'])
                print(item.string)
        
        """
        href=item.attrs['href']
        content=item.string
        print(content+href)
        """
    return


with request.urlopen(fundCompanyList) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
    parseHtmlPage(data.decode('utf-8'))


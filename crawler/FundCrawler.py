from urllib import request
from  utils.FileManager import FileManager
import os

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
            os.makedirs(FileManager.getCurPath()+'/datas/funds/',exist_ok=True)
            filename=FileManager.getCurPath()+'/datas/funds/'+fundName+fundCode+".html"
            with open(filename,'w',encoding='utf-8') as file_obj:
                file_obj.write(utf8data)
        return




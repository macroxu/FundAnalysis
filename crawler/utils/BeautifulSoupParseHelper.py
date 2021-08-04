# Beautiful Soup Parse Helper
class BeautifulSoupParseHelper:
    def __init__(self):
        return

    @staticmethod
    def parseSingleStr(soup,selector,dic,attrName):
        tag=soup.select_one(selector)
        tagValue=''
        #check is existence, if true ,set value,if not ,set default value
        if tag is None:
            tagValue=''
        else:
            tagValue=tag.string
        
        dic[attrName]=tag.string
        return
    
    
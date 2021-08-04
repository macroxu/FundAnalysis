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

    @staticmethod
    def parseArrayStr(soup,selector,dic,attrsName):
        tagList=soup.select(selector)
        # check attrsName'length equal to  taglist's length
        if tagList is None:
            return

        if(len(tagList)!=len(attrsName)):
            #throw exception, //todo
            pass
        for num in range(0,len(tagList)):
            attrName=attrsName[num]
            tagValue=tagList[num].string
            dic[attrName]=tagValue
            
        pass
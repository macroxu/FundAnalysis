import sys
import os
import json

#文件帮助类
class FileManager:
    #获取当前路径
    @staticmethod
    def getCurPath():
        return sys.path[0]


    @staticmethod
    def checkAndCreateDir(dicPath):
        if not os.path.exists(dicPath):
            os.mkdir(dicPath)
        return dicPath

    @staticmethod
    def checkAndCreateRelativeDir(relativeDir):
        fullPath=FileManager.getCurPath()+relativeDir
        os.makedirs(fullPath,exist_ok=True)
        return fullPath

    @staticmethod 
    def saveStringSteamToFile(relativeFileName,strSteam):
        dirPath, fileName = os.path.split(relativeFileName)
        fullDirPath=FileManager.checkAndCreateRelativeDir(dirPath)
        #save to file
        filename=fullDirPath+'/'+fileName
       
        with open(filename,'w',encoding='utf-8') as file_obj:
            file_obj.write(strSteam)

        pass

    @staticmethod
    def readStringSteamToFile(relativeFileName):
        utf8Data=''
        fullFilePath=FileManager.getCurPath()+'/'+relativeFileName;
        with open(fullFilePath,'r',encoding='utf8')as fp:
            utf8Data=fp.read();
        return utf8Data

    @staticmethod
    def buildDirByFilePath(relationFilePath):
        dirPath,fileName=os.path.split(relationFilePath)
        FileManager.checkAndCreateRelativeDir(dirPath)

    
    @staticmethod
    def saveDicAsJsonToFile(relativeFileName,dicData):
        fullFilePath=FileManager.getCurPath+'/'+relativeFileName
        buildDirByFilePath(relativeFileName)

        with open(fullFilePath,'w',encoding='utf8')as fp:
            json.dump(dicData,fp,ensure_ascii='false')

        pass


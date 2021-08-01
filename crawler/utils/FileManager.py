import sys
import os


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



         

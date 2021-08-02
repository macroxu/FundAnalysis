import logging
import os
from logging import handlers

from utils.FileManager import FileManager
_crawlerLogName="crawlerLog"
_crawlerLogFileName='crawlerLog.log'
_crawlerDebugLogFileName='crawlerDebugLog.log'


def _loggingConfig(**kwargs):
    level=kwargs.pop('level',None)
    dateFmt=kwargs.pop('dateFmt',None)
    format=kwargs.pop('format',None)
    if level is None:
        level=logging.DEBUG
    if dateFmt is None:
        dateFmt='%Y-%m-%d %H:%M:%S'
    if format is None:
        format='%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s'
    
    log= logging.getLogger(_crawlerLogName)
    format_str=logging.Formatter(format,dateFmt);
    logDir=FileManager.getCurPath()+"/logs"
    os.makedirs(logDir,exist_ok=True)

    '''
    th_debug=handlers.TimedRotatingFileHandler(filename=logDir+"/"+_crawlerDebugLogFileName,when='D',backupCount=5,encoding='utf-8')
    th_debug.suffix="%Y-%m-%d.log"
    th_debug.setFormatter(format_str)
    th_debug.setLevel(logging.DEBUG)
    #log.addHandler(th_debug)
    #目前不设置debug日志
    '''
    #日志文件信息
    th = handlers.TimedRotatingFileHandler(filename=logDir+"/"+_crawlerLogFileName, when='D', backupCount=3, encoding='utf-8')
    th.suffix = "%Y-%m-%d.log"
    th.setFormatter(format_str)
    th.setLevel(logging.INFO)
    log.addHandler(th)

    #创建一个steam流 显示到屏幕上
    sh = logging.StreamHandler()#往屏幕上输出
    sh.setFormatter(format_str) #设置屏幕上显示的格式
    log.addHandler(sh)
    log.setLevel(logging.ERROR)
    return log

def _exeLoggingConfig(**kwargs):
    logger = _loggingConfig()

def _getLogger():
    return logging.getLogger('crawlerLog')

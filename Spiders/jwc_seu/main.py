from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import pandas as pd


def GetHtmlList(ReUrl, quData, ReHeader):
    '''
    We can get html lists by using urls
    '''
    try:
        r = requests.post(url = ReUrl, data = quData, headers = ReHeader)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"

def GetDataFrameList(Html_List):
    '''
    We can get Datalist by using html 
    '''
    soup = BeautifulSoup(Html_List, 'html.parser')
    souplist = soup.find_all(attrs = {'width' : "20%", 'align': 'left'})
    projects = []
    data = []
    for li in souplist:
        projects.append(li.text.split(':')[0])
        data.append(li.text.split(':')[1])
    myDataFrame = pd.DataFrame([[data[0], data[1], data[2], data[3], data[4]]], index = [1], columns = projects)
    return myDataFrame

def DataSave(DataList):
    '''
    Save the data on differet ways
    '''
    DataList.to_excel('ceshi.xlsx')

def GetqueryData(qSI):
    '''
    like the main function
    '''
    ReqHeader = {
        "Host": "xk.urp.seu.edu.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    }
    ReqUrl = "http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action"
    queryData = {
        "returnStr":"",
        "queryStudentId": "213180001",
        "queryAcademicYear": "20-21-3",
    }
    DFL = pd.DataFrame()
    queryData["queryStudentId"] = str(213180000 + qSI)
    HtmlList = GetHtmlList(ReUrl = ReqUrl, quData = queryData, ReHeader = ReqHeader)
    DFL = DFL.append(GetDataFrameList(Html_List = HtmlList))
    return DFL
if __name__ == '__main__':
    '''
    main function
    '''
    DF = pd.DataFrame()
    pool = Pool(16)
    iter = range(1, 100, 1)
    DF = DF.append(pool.map(GetqueryData, iter), ignore_index = True)
    DataSave(DF)

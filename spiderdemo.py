import random
from urllib import response
from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据s
import time
import pandas as pd


def main():
    datalist = getData()
    savepath = ""
    saveData(datalist,savepath)

def getData():

    type1 = []
    type2 = []
    type3 = []
    type4 = []
    type5 = []
    type6 = []
    type7 = []
    type8 = []
    type9 = []
    type10 = []
    type11 = []
    type12 = []
    type13 = []
    type14 = []
    type15 = []
    type16 = []
    type17 = []
    type18 = []
    type19 = []
    type20 = []


 
    # with open(".\demo\data.txt", "r",encoding='utf-8') as f:  # 打开文件
    #     data = f.read()  # 读取文件
    # html = data
    baseurl = "http://59.110.42.206/BUS_MANAGE1/php/getBusInfo.php?line_name=301&up_or_down=0"
    html = askURL(baseurl)
    # print(html)
    
    # nm = re.compile('"nm":"(.*?)","pid"')#id
    # pid = re.compile('"pid":(.*?),"ic"')#
    # ic = re.compile('"ic":(.*?),"pt": "Yellow Card"')
    # pt = re.compile('"pt":"(.*?)"},{"id"')#

    busNO = re.compile('"busNO":"(.*?)","busState"')
    busState = re.compile('"busState":"(.*?)","up_down"')
    up_down = re.compile('"up_down":"(.*?)","busToUserSelectStationDistance"')
    busToUserSelectStationDistance = re.compile('"busToUserSelectStationDistance":"(.*?)","angle"')
    angle = re.compile('"angle":"(.*?)","lineId"')
    lineId = re.compile('"lineId":"(.*?)","longitude"')
    longitude = re.compile('"longitude":"(.*?)","latitude"')
    latitude = re.compile('"latitude":"(.*?)","nextStationSequnce"')
    nextStationSequnce = re.compile('"nextStationSequnce":"(.*?)","inStationNow"')
    inStationNow = re.compile('"inStationNow":"(.*?)","busToNextStationDistance"')
    busToNextStationDistance = re.compile('"busToNextStationDistance":"(.*?)","currentVelocity"')
    currentVelocity = re.compile('"currentVelocity":"(.*?)","signalStrength"')
    signalStrength = re.compile('"signalStrength":"(.*?)","runningDistance"')
    runningDistance = re.compile('"runningDistance":"(.*?)","busTemp"')
    busTemp = re.compile('"busTemp":"(.*?)","height"')
    height = re.compile('"height":"(.*?)","occurTime"')
    occurTime = re.compile('"occurTime":"(.*?)","orign"')
    orign = re.compile('"orign":"(.*?)","des"')
    des = re.compile('"des":"(.*?)","nextStationName"')
    nextStationName = re.compile('"nextStationName":"(.*?)"}')

    type1.extend(busNO.findall(html))
    type2.extend(busState.findall(html))
    type3.extend(up_down.findall(html))
    type4.extend(busToUserSelectStationDistance.findall(html))
    type5.extend(angle.findall(html))
    type6.extend(lineId.findall(html))
    type7.extend(longitude.findall(html))
    type8.extend(latitude.findall(html))
    type9.extend(nextStationSequnce.findall(html))
    type10.extend(inStationNow.findall(html))
    type11.extend(busToNextStationDistance.findall(html))
    type12.extend(currentVelocity.findall(html))
    type13.extend(signalStrength.findall(html))
    type14.extend(runningDistance.findall(html))
    type15.extend(busTemp.findall(html))
    type16.extend(height.findall(html))
    type17.extend(occurTime.findall(html))
    type18.extend(orign.findall(html))
    type19.extend(des.findall(html))
    type20.extend(nextStationName.findall(html))



    # print(type_one)

    
    dict = {
       #  'nm':type_one,
       # 'pid':type_two,
       # 'ic':type_three,
       # 'pt':type_four


        'busNO':type1,
        'busState':type2,
        'up_down':type3,
        'busToUserSelectStationDistance':type4,
        'angle':type5,
        'lineId':type6,
        'longitude':type7,
        'latitude':type8,
        'nextStationSequnce':type9,
        'inStationNow':type10,
        'busToNextStationDistance':type11,
        'currentVelocity':type12,
        'signalStrength':type13,
        'runningDistance':type14,
        'busTemp':type15,
        'height':type16,
        'occurTime':type17,
        'orign':type18,
        'des':type19,
        'nextStationName':type20

    }

    new_frame = pd.DataFrame.from_dict(dict,orient='index')
    new_frame = new_frame.T
    new_frame.to_csv('.\data.csv')
    # new_frame.to_excel('taobao02.xlsx')
    # print(new_frame)


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "referer":"http://59.110.42.206/BUS_MANAGE1/php/getBusInfo.php?line_name=301&up_or_down=0",
        #"cookie":"SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; JSESSIONID=9F96960DE8BA66161A4248178C873938"
        }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(datalist,savepath):
    print("save...")


if __name__ == "__main__":
    main()
    print("爬取完毕！")
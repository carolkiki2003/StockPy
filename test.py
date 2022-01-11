import requests
from io import StringIO
import pandas as pd
import numpy as np
import datetime

def tester(sid):

    # today = datetime.date.today().strftime('%Y%m%d')
    today='20220110'

    # 下載股價
    r = requests.post('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=csv&date='+ today +'&stockNo='+ sid)

    # 整理資料，變成表格
    # df = pd.read_csv(StringIO(r.text.replace("=", "")), header=["日期" in l for l in r.text.split("\n")].index(True)-1)
    
    df = pd.read_csv(StringIO(r.text.replace("=", "")))
    # 顯示出來
    return df
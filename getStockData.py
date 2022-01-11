import pandas_datareader as pdr
import twstock

def Stocker(sid):
    stock = pdr.DataReader(str(sid)+'.TW', 'yahoo','2022-01-06','2022-01-10')
    return stock

def Advisor(sid):
    stock = twstock.Stock(sid)
    bfp = twstock.BestFourPoint(stock)
    #判斷是否為四大買點
    # return bfp.best_four_point_to_buy()
    #判斷是否為四大賣點
    # return bfp.best_four_point_to_sell()
    #綜合判斷
    return bfp.best_four_point()
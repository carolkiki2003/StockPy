import re
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import redirect
from getStockData import Stocker,Advisor
from test import tester
import pandas as pd

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if input_check(request.form['sid']):
            return redirect(url_for('result', sid=request.form.get('sid')))
        else:
            return redirect(url_for('error', sid=request.form.get('sid')))
    return render_template('index.html')

def input_check(sid):
    # 檢核輸入股票代號
    stock_format = re.compile(r'^[0-9]{4}$')
    if bool(re.match(stock_format,sid)):
        return True
    else:
        return False

@app.route('/result/<sid>')
def result(sid):
    # df=pd.DataFrame(Stocker(sid))
    # new_df = df.drop(["Adj Close"], axis=1)
    # advice=Advisor(sid)
    df=pd.DataFrame(tester(sid))
    df=df.drop(index=['ETF證券代號第六碼為K、M、S、C者，表示該ETF以外幣交易。','當日統計資訊含一般、零股、盤後定價、鉅額交易，不含拍賣、標購。','符號說明:+/-/X表示漲/跌/不比價','說明:'])
    return render_template('result.html', alltable=[df.to_html(classes='alldata')])

@app.route('/error/<sid>')
def error(sid):
    return render_template('error.html', sid=sid)

if __name__=='__main__':
    app.debug = True
    app.secret_key="Your Key"
    app.run()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:52:28 2021

@author: canbeyz
"""

import yfinance
from googletrans import Translator
trans = Translator()

def tocn(content):
    result = trans.translate(content,'zh-cn')
    return result.text
    

stockid = input('请输入股票代码： ')
stock = yfinance.Ticker(stockid)

#for key,value in stock.info.items():
   #print(key,':',value)
   
   
   
print('单位：美元')
print('股票名称： '+ tocn(stock.info['longName']))
print('国家： '+tocn(stock.info['country']))

print('板块： '+tocn(stock.info['sector']))
print('行业： '+tocn(stock.info['industry']))
print('简介： '+tocn(stock.info['longBusinessSummary']))

print('现价： '+str(stock.info['currentPrice']))
print('总收入： '+ str(stock.info['totalRevenue']/10000)+'万元')
print('毛利润： '+str(stock.info['grossProfits']/10000)+'万元')
print('毛利率： '+str(stock.info['grossMargins']))
print('利润率： '+ str(stock.info['profitMargins']))
print('市值： '+str(stock.info['marketCap']/10000)+'万元')
print('成交量： '+ str(stock.info['volume']/10000)+'万元')
print('市盈率： '+ str(stock.info['trailingPE']))
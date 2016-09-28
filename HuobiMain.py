#coding=utf-8

from huobiUtil import *
import HuobiService
import json
import urllib2
import time

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

#初始化apikey，secretkey,url
okcoinapikey = '34ec1779-3f51-498f-8527-99236cb2d329'
okcoinsecretkey = '4797578AC12F053E7263C1D14742A47F'
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,okcoinapikey,okcoinsecretkey)

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,okcoinapikey,okcoinsecretkey)


if __name__ == "__main__":
    '''
    response = urllib2.urlopen('http://api.huobi.com/staticmarket/ticker_btc_json.js')
    html = response.read()
    print html
    print "获取账号详情"
    temp=[]
    temp.append(HuobiService.getAccountInfo(ACCOUNT_INFO))
    print temp[0]
    print temp[0][u'msg']
    '''
    #print HuobiService.getAccountInfo(ACCOUNT_INFO)
    for i in range(1,100000):
        HuobiR = json.loads(HuobiService.getRealTimeDealInfo(ACCOUNT_INFO))
        OkCoinR = (okcoinSpot.ticker('btc_usd'))
        #print HuobiR
        #print OkCoinR
        if int(HuobiR["time"]) == int(OkCoinR['date']):
            print "huobi sell:" + str(HuobiR["ticker"]["sell"]) + "," + "okcoin buy:" + str((OkCoinR["ticker"]["buy"]))
            print "huobi buy:" + str(HuobiR["ticker"]["buy"]) + "," + "okcoin sell:" + str((OkCoinR["ticker"]["sell"]))
            #print float(HuobiR["ticker"]["buy"]) - float(OkCoinR["ticker"]["buy"])
        time.sleep(1)
        #print json.dumps(HuobiService.getRealTimeDealInfo(ACCOUNT_INFO))
        #print (okcoinSpot.ticker('btc_usd'))
"""
    print "提交限价单接口"
    print HuobiService.buy(1,"2355","0.01",None,None,BUY)
    print "提交市价单接口"
    print HuobiService.buyMarket(2,"30",None,None,BUY_MARKET)
    print "取消订单接口"
    print HuobiService.cancelOrder(1,68278313,CANCEL_ORDER)
    print "获取账号详情"
    print HuobiService.getAccountInfo(ACCOUNT_INFO)
    print "查询个人最新10条成交订单"
    print HuobiService.getNewDealOrders(1,NEW_DEAL_ORDERS)
    print "根据trade_id查询order_id"
    print HuobiService.getOrderIdByTradeId(1,274424,ORDER_ID_BY_TRADE_ID)
    print "获取所有正在进行的委托"
    print HuobiService.getOrders(1,GET_ORDERS)
    print "获取订单详情"
    print HuobiService.getOrderInfo(1,68278313,ORDER_INFO)
    print "现价卖出"
    print HuobiService.sell(2,"22.1","0.2",None,None,SELL)
    print "市价卖出"
    print HuobiService.sellMarket(2,"1.3452",None,None,SELL_MARKET)
"""


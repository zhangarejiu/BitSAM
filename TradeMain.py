#coding=utf-8

from huobiUtil import *
import HuobiService
import json
import urllib2
import time
import numpy

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
def avg_list(nlist):
    narray=numpy.array(nlist)
    sum1=narray.sum()
    narray2=narray*narray
    sum2=narray2.sum()
    mean=sum1/len(nlist)
    var=sum2/len(nlist)-mean**2
    return mean

def var_list(nlist):
    narray=numpy.array(nlist)
    sum1=narray.sum()
    narray2=narray*narray
    sum2=narray2.sum()
    mean=sum1/len(nlist)
    var=sum2/len(nlist)-mean**2
    return var
#Sell coin in OKcoin and buy coin in Huobi
def TradeO2H(OkcoinU,HuobiU,OkcoinWave,HuobiWave,Tcount):
    Okstatus = 99
    OkDownCount = 0
    OkTcount = Tcount
    while (Okstatus!=2):
        OkcoinSP = OkcoinU.ticker('btc_usd')['ticker']['buy']
        print  "Okcoin buy price: "+ str(OkcoinSP)
        orderOk = json.loads(OkcoinU.trade('btc_cny','sell',str(float(OkcoinSP)-OkcoinWave),str(OkTcount)))
        print orderOk
        if orderOk['result'] == False:
            break
        time.sleep(3)
        print OkcoinU.orderinfo('btc_cny',orderOk['order_id'])
        print type(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))

        OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
        print OkstatusOrder
        Okstatus = OkstatusOrder['status']
        if(Okstatus!=2):
            OkcoinU.cancelOrder('btc_cny',orderOk['order_id'])
            OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
            OkDownCount = OkstatusOrder['deal_amount']
            OkTcount -= OkDownCount
    HuobiSP = json.loads(HuobiU.getRealTimeDealInfo(ACCOUNT_INFO))["ticker"]["sell"]
    print  "Huobi sell price: "+ str(HuobiSP)
    HuobiOk = HuobiU.buy('1',HuobiSP,str(Tcount),'zsdc1213',None,'buy')
    print HuobiOk
    #print HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info')
    #print type(HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info'))
    return 0
#Sell coin in Huobi and buy coin in OKcoin
def TradeH2O(OkcoinU,HuobiU,OkcoinWave,HuobiWave,Tcount):
    Okstatus = 99
    OkDownCount = 0
    OkTcount = Tcount
    while (Okstatus!=2):
        OkcoinSP = OkcoinU.ticker('btc_usd')['ticker']['sell']
        print "Okcoin sell price: "+ str(OkcoinSP)
        orderOk = json.loads(OkcoinU.trade('btc_cny','buy',str(float(OkcoinSP)-OkcoinWave),str(OkTcount)))
        print orderOk
        if orderOk['result'] == False:
            break
        time.sleep(1)
        print OkcoinU.orderinfo('btc_cny',orderOk['order_id'])
        print type(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))

        OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
        print OkstatusOrder
        Okstatus = OkstatusOrder['status']
        if(Okstatus!=2):
            OkcoinU.cancelOrder('btc_cny',orderOk['order_id'])
            OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
            OkDownCount = OkstatusOrder['deal_amount']
            OkTcount -= OkDownCount
    HuobiSP = json.loads(HuobiU.getRealTimeDealInfo(ACCOUNT_INFO))["ticker"]["buy"]
    print "huobi buy price:" + str(HuobiSP)
    HuobiOk = HuobiU.sell('1',HuobiSP,str(Tcount),'zsdc1213',None,'sell')
    print HuobiOk
    #print HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info')
    #print type(HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info'))
    return 0
def BuyOkcoin(OkcoinU,OkcoinWave,Tcount):
    Okstatus = 99
    OkDownCount = 0
    OkTcount = Tcount
    while (Okstatus!=2):
        OkcoinSP = OkcoinU.ticker('btc_usd')['ticker']['sell']
        print "Okcoin sell price: "+ str(OkcoinSP)
        orderOk = json.loads(OkcoinU.trade('btc_cny','buy',str(float(OkcoinSP)-OkcoinWave),str(OkTcount)))
        print orderOk
        if orderOk['result'] == False:
            break
        time.sleep(1)
        print OkcoinU.orderinfo('btc_cny',orderOk['order_id'])
        print type(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))

        OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
        print OkstatusOrder
        Okstatus = OkstatusOrder['status']
        if(Okstatus!=2):
            OkcoinU.cancelOrder('btc_cny',orderOk['order_id'])
            OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
            OkDownCount = OkstatusOrder['deal_amount']
            OkTcount -= OkDownCount
    return 0



def SellOkcoin(OkcoinU,OkcoinWave,Tcount):
    Okstatus = 99
    OkDownCount = 0
    OkTcount = Tcount
    while (Okstatus!=2):
        OkcoinSP = OkcoinU.ticker('btc_usd')['ticker']['buy']
        print "Okcoin sell price: "+ str(OkcoinSP)
        orderOk = json.loads(OkcoinU.trade('btc_cny','sell',str(float(OkcoinSP)-OkcoinWave),str(OkTcount)))
        print orderOk
        if orderOk['result'] == False:
            break
        time.sleep(1)
        print OkcoinU.orderinfo('btc_cny',orderOk['order_id'])
        print type(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))

        OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
        print OkstatusOrder
        Okstatus = OkstatusOrder['status']
        if(Okstatus!=2):
            OkcoinU.cancelOrder('btc_cny',orderOk['order_id'])
            OkstatusOrder = json.loads(OkcoinU.orderinfo('btc_cny',orderOk['order_id']))['orders'][0]
            OkDownCount = OkstatusOrder['deal_amount']
            OkTcount -= OkDownCount
    return 0

def SellHuobi(HuobiU,HuobiWave,Tcount):
    HuobiSP = json.loads(HuobiU.getRealTimeDealInfo(ACCOUNT_INFO))["ticker"]["buy"]
    print "huobi buy price:" + str(HuobiSP)
    HuobiOk = HuobiU.sell('1',HuobiSP,str(Tcount),'zsdc1213',None,'sell')
    print HuobiOk
    #print HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info')
    #print type(HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info'))
    return 0

def BuyHuobi(HuobiU,HuobiWave,Tcount):
    HuobiSP = json.loads(HuobiU.getRealTimeDealInfo(ACCOUNT_INFO))["ticker"]["sell"]
    print "huobi buy price:" + str(HuobiSP)
    HuobiOk = HuobiU.buy('1',HuobiSP,str(Tcount),'zsdc1213',None,'buy')
    print HuobiOk
    #print HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info')
    #print type(HuobiU.getOrderInfo('1',HuobiOk['id'],'order_info'))
    return 0

def banlance(OkcoinU,HuobiU,flag):
    if flag==0:
        return 0
    OkCoinUInfo = json.loads(OkCoinUser.userinfo())
    OkCoinBtNum = OkCoinUInfo['info']['funds']['free']['btc']
    HuobiUInfo = HuobiService.getAccountInfo(ACCOUNT_INFO)
    HuobiBtNum = HuobiUInfo['available_btc_display']

    while((float(OkCoinBtNum) + float(HuobiBtNum))!=0.2): 
        print "balance: " + "OkCoinBtNum: " + str(OkCoinBtNum) + "HuobiBtNum: " + str(HuobiBtNum)
        if(float(OkCoinBtNum)==0.13 and float(HuobiBtNum)==0.1):
            if banlance_flag == 1:
                print "try to sell huobi 0.03"
                SellHuobi(HuobiU,0,0.03)
            if banlance_flag == 2:
                print "try to sell Okcoin 0.03"
                SellOkcoin(OkcoinU,0,0.03)

        if(float(OkCoinBtNum)==0.1 and float(HuobiBtNum)==0.07):
            if banlance_flag == 1:
                BuyOkcoin(OkcoinU,0,0.03)
                print "try to buy Okcoin 0.03"
            if banlance_flag == 2:
                BuyHuobi(HuobiU,0,0.03)
                print "try to buy huobi 0.03"

        if(float(OkCoinBtNum)==0.1 and float(HuobiBtNum)==0.13):
            print "try to sell huobi 0.03"
            SellHuobi(HuobiU,0,0.03)
        if(float(OkCoinBtNum)==0.07 and float(HuobiBtNum)==0.1):
            print "try to buy okcoin 0.03"
            BuyOkcoin(OkcoinU,0,0.03)
        OkCoinUInfo = json.loads(OkCoinUser.userinfo())
        OkCoinBtNum = OkCoinUInfo['info']['funds']['free']['btc']
        HuobiUInfo = HuobiService.getAccountInfo(ACCOUNT_INFO)
        HuobiBtNum = HuobiUInfo['available_btc_display']
        time.sleep(1)
    return 0
Hs_Ob_cover = []
Hb_Os_cover = []
OkcoinRBuy = 9999
if __name__ == "__main__":
    OkCoinUser = OKCoinSpot(okcoinRESTURL,okcoinapikey,okcoinsecretkey)
    banlance_flag=2
    while(1):
        time.sleep(0.5)
        OkCoinUInfo = json.loads(OkCoinUser.userinfo())
        OkCoinBtNum = float(OkCoinUInfo['info']['funds']['free']['btc'])
        OkCoinCash = float(OkCoinUInfo['info']['funds']['free']['cny'])
        print "OkCoinBtNum: " + str(OkCoinBtNum)
        HuobiUInfo = HuobiService.getAccountInfo(ACCOUNT_INFO)
        for x in HuobiUInfo.values():
            print x
        print HuobiUInfo
        HuobiBtNum = float(HuobiUInfo['available_btc_display'])
        HuobiCash = float(HuobiUInfo['available_cny_display'])
        print "HuobiBtNum: "+ str(HuobiBtNum)
        HuobiR = json.loads(HuobiService.getRealTimeDealInfo(ACCOUNT_INFO))
        OkCoinR = (okcoinSpot.ticker('btc_usd'))
        HuobiRSell = float(HuobiR["ticker"]["sell"])
        OkCoinRSell = float(OkCoinR["ticker"]["sell"])
        HuobiRBuy = float(HuobiR["ticker"]["buy"])
        OkCoinRBuy = float(OkCoinR["ticker"]["buy"])
        Hs_Ob_cover.append(HuobiRSell-OkCoinRBuy)
        Hb_Os_cover.append(HuobiRBuy-OkCoinRSell)
        if((float(OkCoinBtNum) + float(HuobiBtNum))!=0.2):
            banlance(OkCoinUser,HuobiService,banlance_flag)
        print "huobisell:" + str(HuobiRSell) + "," + "okcoinbuy:" + str((OkCoinRBuy))
        print "huobibuy:" + str(HuobiRBuy) + "," + "okcoinsell:" + str((OkCoinRSell))
        if len(Hs_Ob_cover)>500:
            print "profile: " + str(HuobiCash+OkCoinCash - 101.06 - 99.45)
            time.sleep(1)
            flag = 500
            if len(Hs_Ob_cover)>1000:
                flag = 1000
            
            if len(Hs_Ob_cover)>2000:
                flag = 2000
            temp_list_hob = [Hb_Os_cover[i] for i in range(len(Hs_Ob_cover)-flag,len(Hs_Ob_cover))]
            CoverHoBAvg = avg_list(temp_list_hob)
            CoverHoBVar = var_list(temp_list_hob)
            print "CoverHoBAvg :" + str(CoverHoBAvg)
            print "CoverHoBVar :" + str(CoverHoBVar)
            temp_list_boh = [Hs_Ob_cover[i] for i in range(len(Hs_Ob_cover) - flag,len(Hb_Os_cover))]
            CoverBoHAvg = avg_list(temp_list_boh)
            CoverBoHVar = var_list(temp_list_boh)
            print "CoverBoHAvg :" + str(CoverBoHAvg)
            print "CoverBoHVar :" + str(CoverBoHVar)
            if(HuobiRBuy-OkCoinRSell>CoverHoBAvg+3*CoverHoBVar and
            HuobiBtNum>=OkCoinBtNum):
                TradeH2O(OkCoinUser,HuobiService,0,0,0.03)
                banlance_flag = 1
                OkCoinUInfo = json.loads(OkCoinUser.userinfo())
                OkCoinBtNum = OkCoinUInfo['info']['funds']['free']['btc']
                print "OkCoinBtNum: " + str(OkCoinBtNum)
                HuobiUInfo = HuobiService.getAccountInfo(ACCOUNT_INFO)
                HuobiBtNum = HuobiUInfo['available_btc_display']
                print "HuobiBtNum: "+ str(HuobiBtNum)
                time.sleep(10)
            if(HuobiRSell-OkCoinRBuy<CoverBoHAvg-3*CoverBoHVar and                HuobiBtNum<OkCoinBtNum):
                TradeO2H(OkCoinUser,HuobiService,0,0,0.03)

                banlance_flag = 2
                OkCoinUInfo = json.loads(OkCoinUser.userinfo())
                OkCoinBtNum = OkCoinUInfo['info']['funds']['free']['btc']
                print "OkCoinBtNum: " + str(OkCoinBtNum)
                HuobiUInfo = HuobiService.getAccountInfo(ACCOUNT_INFO)
                HuobiBtNum = HuobiUInfo['available_btc_display']
                print "HuobiBtNum: "+ str(HuobiBtNum)
                time.sleep(10)
    #print HuobiService.getAccountInfo(ACCOUNT_INFO)
    #TradeO2H(OkCoinUser,0,0.01)
    #TradeH2O(OkCoinUser,HuobiService,0,0,0)
    #TradeH2O(OkCoinUser,HuobiService,0,0,0.01)
    #TradeO2H(OkCoinUser,HuobiService,0,0,0.05)
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
    """
    for i in range(1,100000):
        HuobiR = json.loads(HuobiService.getRealTimeDealInfo(ACCOUNT_INFO))
        OkCoinR = (okcoinSpot.ticker('btc_usd'))
        if int(HuobiR["time"]) == int(OkCoinR['date']):
            print float(HuobiR["ticker"]["sell"]) - float(OkCoinR["ticker"]["sell"])
        time.sleep(15)
    """
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


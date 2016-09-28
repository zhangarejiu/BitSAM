#coding=utf-8

import urllib
import hashlib
import hmac
import base64

#在此输入您的Key
ACCESS_KEY="9348b634-d5d7b1a1-9a889aae-48507"
SECRET_KEY="7f08d054-bac9effa-8979eaf2-58c90"

HUOBI_SERVICE_API="https://api.huobi.com/apiv3"


BUY = "buy"
BUY_MARKET = "buy_market"
CANCEL_ORDER = "cancel_order"
ACCOUNT_INFO = "get_account_info"
NEW_DEAL_ORDERS = "get_new_deal_orders"
ORDER_ID_BY_TRADE_ID = "get_order_id_by_trade_id"
GET_ORDERS = "get_orders"
ORDER_INFO = "order_info"
SELL = "sell"
SELL_MARKET = "sell_market"

def signature(params):
    params = sorted(params.iteritems(), key=lambda d:d[0], reverse=False)
    message = urllib.urlencode(params)
    m = hashlib.md5()
    m.update(message)
    m.digest()
    sig=m.hexdigest()
    return sig


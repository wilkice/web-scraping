import requests

url = 'https://api2.dealmoon.com/'

data = {
    "protocolType":"request",
    "protocol":"1.0.42",
    "command":"deal\/deal\/list",
    "clientInfo":{
        "editionId":"9.5.1",
        "subCoopId":"0",
        "softLanguage":"31",
        "platformId":"100028",
        "productId":"1000",
        "romIns":"0"
    },
    "mobileInfo":{
        "model":"SM-N9500",
        "apn":"WIFI",
        "imei":"000000000000000",
        "smsCenter":"0",
        "cellId":"0",
        "imsi":"000000000000000",
        "height":2960,
        "language":"31",
        "width":1440,
        "country":"86",
        "cpu":"armeabi-v7a",
        "accessToken":"b103934fd057d02162cd30b036c1bf03",
        "udid":"000000000000000",
        "device":"Android",
        "rooted":"",
        "systemVersion":"9",
        "idfa":"eb9a79d8-9b04-4e27-a31d-67ed36562ee6"
    },
    "serviceInfo":{
        "resourceUpdateTime":"",
        "activeTime":"",
        "clientId":"10669388"
    },
    "commandInfo":{
        "category":"Electronics-Computers",
        "end":"",
        "page":"1",
        "isTop":False
    }
}
headers = {
# 'DMAuthorization': 'fc45773d42425db36736a2253431afa8',
'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; SM-N9500 Build/PPR1.180610.011)',
'Host': 'api2.dealmoon.com',
}
response = requests.post(url, data=data, headers=headers)
print(response.status_code)


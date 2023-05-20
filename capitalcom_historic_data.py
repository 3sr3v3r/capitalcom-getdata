from capitalcompy import API
from capitalcompy.contrib.factories import EpicCandlesFactory
import capitalcompy.endpoints.session as session
import capitalcompy.endpoints.markets as markets
import pandas as pd
import json
import time
import threading

from Cryptodome.Cipher import PKCS1_v1_5
from Cryptodome.PublicKey import RSA
import base64

#path to write the output .csv files to
path = "./"
#epics list of instruments to grab data for e.g. ['US100']
epics = ['USDJPY']

#Resolution: possible values: MINUTE, MINUTE_5, MINUTE_15, MINUTE_30, HOUR, HOUR_4, DAY, WEEK
resolution = "DAY"

_from = "2023-01-03T08:00:00"

_to= "2023-05-18T00:00:00"

#Get the bid or ask price.
bidask = 'bid'

#Number of bars to retrieve in each partial call (max 1000 for Capital.com)
maxbars = 500

download = True
show_instruments = False
export_format_forextester = False

def encryptPasswd(encryptionkey, timestamp, password):
    input = password + '|' + str(timestamp)
    input = base64.b64encode(str.encode(input))
    key = str.encode(encryptionkey)
    key = base64.b64decode(key)
    key = RSA.import_key(key)
    cipher = PKCS1_v1_5.new(key)

    ciphertext = bytes.decode(base64.b64encode(cipher.encrypt(input)))
    return ciphertext


def ping_function():
    while sessionrunning:
        time.sleep(300)
        r = session.Ping()
        rv = client.request(r)
        print("ping result: " + str(rv))
        if not sessionrunning:
            print("Finishing ping thread.")

def getnodes(nodeid):
    r = markets.Getnodes(nodeid)
    return client.request(r)


with open("config_capitalcom.json", "r") as file:
    config = json.load(file)

apikey = config["capitalcom"]["apikey"]
accountID = config["capitalcom"]["account"]
password = config["capitalcom"]["password"]
environment = config["capitalcom"]["environment"]
client = API(apikey=apikey, environment=environment)

'First get the encryption key from the API. Input is the apikey and it returns an encryptionkey to be used to send'
'the password encrypted'
r = session.GetEncryptionKey()
rv = client.request(r)

'to obtain a valid session token the password concatenated with a "|" and timestamp are encrypted'
password = encryptPasswd(rv['encryptionKey'], rv['timeStamp'], password)

'start a session. apikey and encrypted password yields an authentication token (CST) and an account identifier'
'X-SECURITY-TOKEN'
data = '{"encryptedPassword": "true", "identifier": "'+ accountID + '", "password": "'+ password+'"}'
r = session.StartSession(data=data)
rv = client.request(r)

sessionrunning = True
x = threading.Thread(target=ping_function, args=())
x.daemon = True
x.start()

if show_instruments:
    result_list = []
    r = markets.Marketnavigation('none')
    nodes0 = client.request(r)

    for node0 in nodes0['nodes']:
        nodeid = (node0['id'])

        nodes1 = getnodes(nodeid)
        for node1 in nodes1['nodes']:
            nodes2 = getnodes(node1['id'])
            level_response = pd.json_normalize(node1)
            result_list.append(level_response)

            if 'markets' in nodes2:
                level_response = pd.json_normalize(nodes2, record_path=['markets'])
                if not level_response.empty:
                    result_list.append(level_response)
            else:
                level_response = pd.json_normalize(nodes2, record_path=['nodes'])
                if len(nodes2['nodes']) > 0:
                    for node2 in nodes2['nodes']:
                        nodes3 = getnodes(['id'])
                        'add a sleep timer to prevent hitting the 10 api calls per second limit'
                        time.sleep(0.100)
                        if len(nodes3) > 1:
                            level_response = pd.json_normalize(nodes3, record_path=['markets'])
                            result_list.append(level_response)

    pd.concat(result_list).to_csv(path + 'capitalcom_instruments.csv', index=False)


if download:
    params = {
       "resolution": resolution,
        "max": maxbars,
       "from": _from,
       "to": _to,
    }
    if export_format_forextester:
        for epic in epics:
            # The factory returns a generator generating consecutive
            # requests to retrieve full history from date '_from' till '_to'
            df = pd.DataFrame()
            for r in EpicCandlesFactory(epic=epic, params=params):
                data = client.request(r)
                #check if there is real candle data in the calls. We dont want to stop processing in case of a
                #{"errorCode":"error.prices.not-found"} which is thrown if part of the data is not available.
                if not "errorCode" in data:
                    results = [{"date": x['snapshotTimeUTC'][0:10].replace("-","."), "time": x['snapshotTimeUTC'][11:16],"open": float(x['openPrice'][bidask]), "high": float(x['highPrice'][bidask]),
                                "low": float(x['lowPrice'][bidask]), "close": float(x['closePrice'][bidask]), "volume": int(x['lastTradedVolume'])} for x in
                               data['prices']]
                if len(results) > 0:
                    tmp_df = pd.DataFrame(results)
                    #use df = df.append(tmp_df) for panda version < 2.0
                    df = pd.concat([df, tmp_df])
                    print("last candle: " + df['date'].iloc[-1] + " " + df['time'].iloc[-1])
    else:
        for epic in epics:
            # The factory returns a generator generating consecutive
            # requests to retrieve full history from date '_from' till '_to'
            df = pd.DataFrame()
            for r in EpicCandlesFactory(epic=epic, params=params):
                data = client.request(r)
                #check if there is real candle data in the calls. We dont want to stop processing in case of a
                #{"errorCode":"error.prices.not-found"} which is thrown if part of the data is not available.
                if not "errorCode" in data:
                    results = [{"time": x['snapshotTimeUTC'], "open": float(x['openPrice'][bidask]), "high": float(x['highPrice'][bidask]),
                                "low": float(x['lowPrice'][bidask]), "close": float(x['closePrice'][bidask]), "volume": float(x['lastTradedVolume'])} for x in
                               data['prices']]
                if len(results) > 0:
                    tmp_df = pd.DataFrame(results)
                    # use df = df.append(tmp_df) for panda version < 2.0
                    df = pd.concat([df, tmp_df])
                    print("last candle: " + df['time'].iloc[-1])

    print('writing: ' + path + 'capitalcom_' + epic + '_' + resolution + '.csv')
    df.to_csv(path + 'capitalcom_' + epic + '_' + resolution + '.csv', index=False)


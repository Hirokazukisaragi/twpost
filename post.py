import json

import sys

from requests_oauthlib import OAuth1Session
#please input your token
CK = ''                             # Consumer Key
CS = ''         # Consumer Secret
AT = '' # Access Token
AS = ''         # Accesss Token Secert
com = input()
#ツイート入力
def tpost():
    # ツイート投稿用のURL
    url = "https://api.twitter.com/1.1/statuses/update.json"
    postemp = ""
    post = ""
    while True:
        postemp = sys.stdin.readline()
        if(postemp == ".\n"):
            break
        post += postemp
        postemp = ""
    # ツイート本文
    post = post[:139]
    params = {"status": post}
    twitter = OAuth1Session(CK, CS, AT, AS)
    req = twitter.post(url, params = params)

    # レスポンスを確認
    if req.status_code == 200:
        print ("OK")
    else:
        print ("Error: %d" % req.status_code)

def tget():
    params = {}
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    twitter = OAuth1Session(CK, CS, AT, AS)

    req = twitter.get(url, params=params)
    if req.status_code == 200:
        # レスポンスはJSON形式なので parse する
        timeline = json.loads(req.text)
        twiit = reversed(timeline)

        # 各ツイートの本文を表示
        for tweet in twiit:
            print(tweet["text"])

    else:
        # エラーの場合
        print("Error: %d" % req.status_code)
if com == "get":
    tget()
if com == "post":
    tpost()

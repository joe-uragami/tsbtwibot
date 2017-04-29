import os

import twitter

# API設定は環境変数で指定
api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )

for item in twitter.userstream.user():
    # TLにリプライでTWITTE_IDが含まれてたら分岐
    if item['in_reply_to_screen_name'] == "TWITTER_ID":
        print (item['id_str'])
        print (item['text'])
        tweet = "@" + item['user']['screen_name'] + " "

        # メッセージをランダムに取得

        # リプ返し
        api.PostUpdates(tweet)



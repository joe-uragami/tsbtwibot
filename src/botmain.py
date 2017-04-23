import os

import twitter


# API設定は環境変数で指定
api = twitter.Api(consumer_key=os.environ[""],
                  consumer_secret=os.environ[""],
                  access_token_key=os.environ[""],
                  access_token_secret=os.environ[""]
                  )

api.PostUpdates("ツイートするやつ")
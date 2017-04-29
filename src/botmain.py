import codecs
import os

import sys
import twitter



# API設定は環境変数で指定
api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )


def tweet_random():
    '''
    データを読み込み１件ランダムでツイートする
    :return:
    '''
    # データ取得処理

    # ツイート実行
    api.PostUpdates("ツイートするやつ")


def follow_back():
    '''
    フォローした人をフォローする
    :return:
    '''



def tag_retweet():
    '''
    ハッシュタグを検索してリツイートする
    :return:
    '''




def main(args):
    '''
    メイン処理、引数に応じて処理を実施する
    :param args:
    :return:
    '''

    # ランダムツイート
    tweet_random()

    # フォローしてくれた人をフォロー
    follow_back()

    # ハッシュタグ検索してリツイート
    tag_retweet()


if __name__ == '__main__':
    sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
    args = sys.argv
    main(args)
import codecs
import os

import sys
import twitter

import json
import random
from datetime import datetime, time

# API設定は環境変数で指定
api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )


def tweet_introduction():
    '''
    部活紹介用のデータを読み込み１件ランダムでツイートする
    :return:
    '''
    # データ取得
    f =  open('introduction.json', 'r')
    intro_dict = json.load(f)

    intro = random.choice(intro_dict)

    # ツイート実行
    # 複数の画像ツイートがこれでいいのかは検証が必要
    api.PostUpdates(status = intro['text'], media = intro['img'])


def follow_back():
    '''
    フォローした人をフォローする
    他botで実装済みのためこちらでは実装しない
    :return:
    '''
    pass


def tag_retweet():
    '''
    ハッシュタグを検索してリツイートする
    :return:
    '''
    # データ取得
    f =  open('hashtags.json', 'r')
    tags = json.load(f)

    for tag in tags:
        # タグを検索
        nowtime = int(time.mktime(datetime.now().timetuple()))
        results = api.GetSearch(tarm = tag, count=50, result_type='recent')

        for result in results:
            # 12時間以内の投稿だった場合リツイート
            if result.created_at_in_seconds in range(nowtime-60*60*12, nowtime):
                try:
                    api.PostRetweet(result.id)
                except:
                    print('既にリツイートされています')


def main(args):
    '''
    メイン処理、引数に応じて処理を実施する
    :param args:
    :return:
    '''

    if "ti" in args:
        # ランダムツイート
        tweet_introduction()

    if "fb" in args:
        # フォローしてくれた人をフォロー
        follow_back()

    if "tr" in args:
        # ハッシュタグ検索してリツイート
        tag_retweet()


if __name__ == '__main__':
    sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
    args = sys.argv
    main(args)
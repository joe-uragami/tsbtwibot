# coding:utf-8

import codecs
import os

import sys
import twitter

import json
import random
import time
from datetime import datetime

abs_path = os.path.abspath(os.path.dirname(__file__))


def tweet_introduction(api):
    """
    部活紹介用のデータを読み込み１件ランダムでツイートする
    :param api:Twitter Api
    :return:
    """
    # データ取得
    with open(os.path.join(abs_path, 'introduction.json'), 'r') as f:
        intro_list = json.load(f)

    intro = random.choice(intro_list)

    media_list = [os.path.join(abs_path, 'attachment', media) for media in intro['img']]

    # ツイート実行
    # 複数の画像ツイートがこれでいいのかは検証が必要
    api.PostUpdates(status=intro['text'], media=media_list, media_category=intro['category'])


def follow_back(api):
    """
    フォローした人をフォローする
    他botで実装済みのためこちらでは実装しない
    :param api:Twitter Api
    :return:
    """
    pass


def tag_retweet(api, nowtime, lowertime):
    """
    ハッシュタグを検索してリツイートする
    :param api:Twitter Api
    :param nowtime:現在時間
    :param lowertime:リツイートする範囲の下限時間
    :return:
    """
    # データ取得
    with open(os.path.join(abs_path, 'hashtags.json'), 'r') as f:
        tags = json.load(f)

    for tag in tags:
        # タグを検索
        results = api.GetSearch(term=tag, count=50, result_type='recent')

        for result in results:
            # 自分のツイートでない、12時間以内の投稿だった場合リツイート
            tweet_name = result.user.screen_name
            if lowertime <= result.created_at_in_seconds < nowtime \
                    and not tweet_name == "10932club":
                try:
                    api.PostRetweet(result.id)
                except:
                    # print('既にリツイートされてます')
                    continue



def main(args):
    '''
    メイン処理、引数に応じて処理を実施する
    :param args:
    :return:
    '''
    # API設定は環境変数で指定
    api = twitter.Api(consumer_key=os.environ["TEST_CONSUMER_KEY"],
                      consumer_secret=os.environ["TEST_CONSUMER_SECRET"],
                      access_token_key=os.environ["TEST_ACCESS_TOKEN_KEY"],
                      access_token_secret=os.environ["TEST_ACCESS_TOKEN_SECRET"]
                      )

    # api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
    #                   consumer_secret=os.environ["CONSUMER_SECRET"],
    #                   access_token_key=os.environ["ACCESS_TOKEN_KEY"],
    #                   access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
    #                   )

    if "ti" in args:
        # ランダムツイート
        tweet_introduction(api)

    if "fb" in args:
        # フォローしてくれた人をフォロー
        follow_back(api)

    if "tr" in args:
        # ハッシュタグ検索してリツイート
        nowtime = int(time.mktime(datetime.now().timetuple()))
        lowertime = nowtime-60*60*12
        tag_retweet(api, nowtime, lowertime)


if __name__ == '__main__':
    sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
    args = sys.argv
    main(args)
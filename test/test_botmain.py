# -*- coding: utf-8 -*-

from src.botmain import tweet_introduction, tag_retweet
from mock import MagicMock
import twitter
from unittest import TestCase


class TsbtwibotTest(TestCase):


    def mock_postupdates(self):
        print("つぶやいたよー")

    def test_tweet_introduction_ファイル内容が読めること(self):

        print("開始ー")

        api = twitter.Api()
        api.PostUpdates = MagicMock()
        api.PostUpdates.side_effect = self.mock_postupdates()

        tweet_introduction(api)

        print(api.PostUpdates.call_args_list)

        assert 1

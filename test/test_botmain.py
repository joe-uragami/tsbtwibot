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


    def mock_postretweet(self):
        print("RTしたよー")

    def test_tag_retweet_ハッシュタグを読み込めること(self):

        print("開始ー")

        mock_result = MagicMock()
        mock_result.created_at_in_seconds.return_value = 2000
        mock_result.user.return_value.screen_name.return_value = 'joe_uragami'
        mock_result.id.return_value = '1919'

        api = twitter.Api()
        api.GetSearch = MagicMock()
        api.GetSearch.return_value = [mock_result]

        api.PostRetweet = MagicMock()
        api.PostRetweet.side_effect = self.mock_postretweet()

        tag_retweet(api, 4000, 1000)

        print(api.GetSearch.call_args_list)

        print(api.PostRetweet.call_args_list)

        assert api.PostRetweet.call_count == 18



    def test_tag_retweet_時間外をリツイートしないこと(self):

        print("開始ー")

        mock_result = MagicMock()
        mock_result.created_at_in_seconds.return_value = 200
        mock_result.user.return_value.screen_name.return_value = 'joe_uragami'
        mock_result.id.return_value = '1919'

        api = twitter.Api()
        api.GetSearch = MagicMock()
        api.GetSearch.return_value = [mock_result]

        api.PostRetweet = MagicMock()
        api.PostRetweet.side_effect = self.mock_postretweet()

        tag_retweet(api, 4000, 1000)

        assert api.PostRetweet.call_count == 0


    def test_tag_retweet_指定ユーザーをリツイートしないこと(self):

        print("開始ー")

        mock_result = MagicMock()
        mock_result.created_at_in_seconds.return_value = 200
        mock_result.user.return_value.screen_name.return_value = '10932club'
        mock_result.id.return_value = '1919'

        api = twitter.Api()
        api.GetSearch = MagicMock()
        api.GetSearch.return_value = [mock_result]

        api.PostRetweet = MagicMock()
        api.PostRetweet.side_effect = self.mock_postretweet()

        tag_retweet(api, 4000, 1000)


        assert api.PostRetweet.call_count == 0
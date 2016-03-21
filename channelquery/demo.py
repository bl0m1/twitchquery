#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Docstring """

from twitchchannelquery import twitchchannelquery

channel = twitchchannelquery()
# arg1 is cahnnel, arg2 is follower limit (default 1, max 100) and arg3 is follower offset (default 0)
channel.setup('monstercat')
channel.query_channel()
channel.query_followers()

if channel.is_online():
    print("Channel is online.")
    print("Stream ID:", channel.get_stream_id())
    print("Stream URL:", channel.get_stream_url())
    print("Start time:", channel.get_start_time())
    print("Game:", channel.get_game())
    print("Title:", channel.get_status())
    print("Viewers:", channel.get_viewers())
    print("Total views:", channel.get_views())
    print("Followers:", channel.get_followers())
else:
    print("Channel is offline.")

if channel.get_follower_ready():
        print("Latest follower:", channel.get_followers_list()[0]["user"]["display_name"])
        print("Follower since:", channel.get_followers_list()[0]["created_at"])
        print("follower got notification:", channel.get_followers_list()[0]["notifications"])
        #print("Follower list:", channel.get_followers_list())

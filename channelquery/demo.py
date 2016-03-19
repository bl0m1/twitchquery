#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Docstring """

from twitchchannelquery import twitchchannelquery

channel = twitchchannelquery()
# arg1 is cahnnel, arg2 is follower limit(default 1) and arg3 is follower offset(default 0) (max 50)
channel.setup('monstercat', '2')
channel.query()

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
    print("Follower:", channel.get_follower_name())
    print("Follower since:", channel.get_follower_date())
    print("follower got notification:", channel.get_follower_notification())
    #print("Follower list:", channel.get_follower_list())
else:
    print("Channel is offline.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Docstring """

from twitchchannelquery import twitchchannelquery

channel = twitchchannelquery()
# arg1 is cahnnel and arg2 is follower nr (from the end)
channel.setup('Food', '1')
channel.query()

if channel.is_online():
    print("Channel is online.")
    print("Stream ID:", channel.get_stream_id())
    print("Start time:", channel.get_start_time())
    print("Game:", channel.get_game())
    print("Title:", channel.get_status())
    print("Viewers:", channel.get_viewers())
    print("Total views:", channel.get_views())
    print("Followers:", channel.get_followers())
    print("Follower:", channel.get_follower())
    print("Follower since:", channel.get_followed())
    print("follower got notification:", channel.get_notification())
else:
    print("Channel is offline.")

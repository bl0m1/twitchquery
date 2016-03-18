#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  twitchchannelquery

  Get Twitch channel online data easily.
"""

import requests

class twitchchannelquery(object):
    """ twitchchannelquery

        Attributes:
        * url: Url to Twitch channel API.
        * online: Online status of Twitch channel.
        * raw: Requests data.
        * fraw: Requests data.
        * jsondata: JSON formatted requests data.
        * stream_id: Unique ID for current stream.
        * stream_url: URL to current stream.
        * start_time: Start time of current stream in ISO 8601 format.
        * game: What game is played on current stream.
        * views: Amount of total views on channel.
        * viewers: Current amount of viewers on channel.
        * followers: Amount of followers for channel.
        * status: Status (title) message of stream.
        * follower: Get a follower.
        * followed: Get date when the follower followed you.
        * notification: If the follower getting an notification when the channel go live.
    """

    # pylint: disable=too-many-instance-attributes
    # The amount of attributes is just fine.

    def __init__(self, channel=""):
        """ Initialization. """
        self.url = ("https://api.twitch.tv/kraken/streams/" + channel + "/")
        self.furl =  'https://api.twitch.tv/kraken/channels/' + channel + '/follows?direction=DESC&limit=1&offset=0'
        self.offset = 0
        self.limit = 1
        self.online = False
        self.error = False
        self.raw = requests.Response()
        self.fraw = requests.Response()
        self.jsondata = ""
        self.jsonfdata = ""
        self.stream_id = ""
        self.stream_url = ""
        self.start_time = ""
        self.game = ""
        self.views = ""
        self.viewers = ""
        self.followers = ""
        self.status = ""
        self.follower = ""
        self.followed = ""
        self.notification = ""

    def setup(self, channel="", offset="", limit=""):
        """ Config. """
        self.url = "https://api.twitch.tv/kraken/streams/" + channel + "/"
        self.furl =  'https://api.twitch.tv/kraken/channels/' + channel + '/follows?direction=DESC&limit=' + limit + '&offset=' + offset

    def reset(self):
        """ Reset variables """
        self.online = False
        self.error = False
        self.raw = requests.Response()
        self.fraw = requests.Response()
        self.jsondata = ""
        self.jsonfdata = ""
        self.stream_id = ""
        self.stream_url = ""
        self.start_time = ""
        self.game = ""
        self.views = ""
        self.viewers = ""
        self.followers = ""
        self.status = ""
        self.follower = ""
        self.followed = ""
        self.notification = ""

    def get_raw(self):
        """ Return raw requests data. """
        return self.raw

    def get_fraw(self):
        """ Return raw requests fdata. """
        return self.fraw

    def is_online(self):
        """ Return online status of Twitch channel. """
        return self.online

    def get_stream_id(self):
        """ Return stream id. """
        return self.stream_id

    def get_stream_url(self):
        """ Return URL for stream """
        return self.stream_url

    def get_start_time(self):
        """ Return start time of stream. """
        return self.start_time

    def get_game(self):
        """ Return game played on stream. """
        return self.game

    def get_views(self):
        """ Return total views for channel """
        return self.views

    def get_viewers(self):
        """ Return current amount of viewers for channel """
        return self.viewers

    def get_followers(self):
        """ Return amount of followers for channel """
        return self.followers

    def get_status(self):
        """ Return status message for stream. """
        return self.status

    def get_follower(self):
        """ Return amount of followers for channel """
        return self.follower

    def get_followed(self):
        """ Return the selected follower """
        return self.followed

    def get_notification(self):
        """ Return the selected follower """
        return self.notification

    def send_query(self):
        """ Request URL. """
        try:
            self.raw = requests.get(self.url)
            self.jsondata = self.raw.json()
            self.fraw = requests.get(self.furl)
            self.jsonfdata = self.fraw.json()
        except ConnectionError:
            return False
        except requests.exceptions.HTTPError:
            return False
        return True

    def parse_response(self, data, fdata):
        """ Parse response into variables. """
        if "error" in data:
            self.error = True
        elif "error" in fdata:
            self.error = True
        elif data["stream"] is None:
            pass
        else:
            self.online = True
            self.stream_id = data["stream"]["_id"]
            self.stream_url = data["stream"]["channel"]["url"]
            self.start_time = data["stream"]["created_at"]
            self.game = data["stream"]["game"]
            self.views = data["stream"]["channel"]["views"]
            self.viewers = data["stream"]["viewers"]
            self.followers = data["stream"]["channel"]["followers"]
            self.status = data["stream"]["channel"]["status"]
            self.follower = fdata['follows'][0]['user']['display_name']
            self.followed = fdata['follows'][0]['created_at']
            self.notification = fdata['follows'][0]['notifications']

    def query(self):
        """ Query Twitch for channel. """
        if self.send_query():
            self.parse_response(self.jsondata, self.jsonfdata)

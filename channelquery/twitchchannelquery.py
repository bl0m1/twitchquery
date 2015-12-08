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
        * jsondata: JSON formatted requests data.
        * stream_id: Unique ID for current stream.
        * stream_url: URL to current stream.
        * start_time: Start time of current stream in ISO 8601 format.
        * game: What game is played on current stream.
        * views: Amount of total views on channel.
        * viewers: Current amount of viewers on channel.
        * followers: Amount of followers for channel.
        * status: Status (title) message of stream.
    """

    # pylint: disable=too-many-instance-attributes
    # The amount of attributes is just fine.

    def __init__(self, url=""):
        """ Initialization. """
        self.url = url
        self.online = False
        self.error = False
        self.raw = requests.Response()
        self.jsondata = ""
        self.stream_id = ""
        self.stream_url = ""
        self.start_time = ""
        self.game = ""
        self.views = ""
        self.viewers = ""
        self.followers = ""
        self.status = ""

    def setup(self, url=""):
        """ Config. """
        self.url = url

    def reset(self):
        """ Reset variables """
        self.online = False
        self.error = False
        self.raw = requests.Response()
        self.jsondata = ""
        self.stream_id = ""
        self.stream_url = ""
        self.start_time = ""
        self.game = ""
        self.views = ""
        self.viewers = ""
        self.followers = ""
        self.status = ""

    def get_raw(self):
        """ Return raw requests data. """
        return self.raw

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

    def send_query(self):
        """ Request URL. """
        try:
            self.raw = requests.get(self.url)
            self.jsondata = self.raw.json()
        except ConnectionError:
            return False
        except requests.exceptions.HTTPError:
            return False
        return True

    def parse_response(self, data):
        """ Parse response into variables. """
        if "error" in data:
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

    def query(self):
        """ Query Twitch for channel. """
        if self.send_query():
            self.parse_response(self.jsondata)

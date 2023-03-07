# -*- coding: utf-8 -*-
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.Settings import FollowersOrder
import os

from flask import Flask, jsonify, request
from guessit import guessit

import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    channels = os.environ.get("channels")
    twitch_miner = TwitchChannelPointsMiner(
        username=os.environ.get("username"),
        password=os.environ.get("password"),            # If no password will be provided, the script will ask interactively
        claim_drops_startup=True,                  # If you want to auto claim all drops from Twitch inventory on the startup
    )
    twitch_miner.mine(channels.split(','), followers=False) 

if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 8000))
    app.run()

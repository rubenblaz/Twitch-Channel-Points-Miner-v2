# -*- coding: utf-8 -*-
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.Settings import FollowersOrder
import os

from flask import Flask, jsonify, request
from guessit import guessit

import sys

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
    
@app.route('/stop')
def stop():
    sys.exit(4)
    
@app.route('/parse', methods=['POST'])
def parse():
    filename = request.get_json()
    print(filename)

    #pretty_names = PTN.parse(filename)
    pretty_names = guessit(filename)
    pretty_names.pop('language', None)
    pretty_names.pop('country', None)
    print(pretty_names)
    #aux = pretty_names.split(', ')
    return jsonify(pretty_names)

if __name__ == '__main__':
    #port = int(os.environ.get('PORT', 8000))
    app.run()

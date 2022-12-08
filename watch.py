# -*- coding: utf-8 -*-
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.classes.Settings import FollowersOrder
import os

from flask import Flask, jsonify, request
#import PTN
import os
from guessit import guessit

channels = "rocketleague,eltitoyoutube,rocketleagueapac,rocketleagueoce,rocketbaguette,rocketbenelux,rocketstreetlive,knockoutcity,EASPORTSFIFA,hustle,Tocata,robz,ZepXP,lobapsd,elded,weplayrocketleague,theorderofdylan,katiepeircee,hitbotc,rageatreyu,behavingbeardly,nateacuiki,nexergames,enviosity"

twitch_miner = TwitchChannelPointsMiner(
        username="rublr",
        password="A123456789a",            # If no password will be provided, the script will ask interactively
        claim_drops_startup=True,                  # If you want to auto claim all drops from Twitch inventory on the startup
)
twitch_miner.mine(channels.split(','), followers=False) 

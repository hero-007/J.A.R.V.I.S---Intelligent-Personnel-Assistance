""" This module is used to play a random music file from the selected directory
    when user ask to play a random song """

import os
import random as ran
import webbrowser as wb


def play_random_music():
    song_list = os.listdir('E:\\Music')
    i = ran.choice(song_list)
    wb.open('E:\\Music\\'+i)
    return

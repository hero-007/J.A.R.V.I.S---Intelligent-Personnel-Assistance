import speech_recognition as sr
import win32com.client
import ctypes
import winshell
from nltk.tokenize import word_tokenize as wtk
from nltk.tokenize import sent_tokenize as srtk
import random as ran
import os

# J.A.R.V.I.S Modules
import extra_system_feature as esf
import open_app_feature as oaf
import random_music_play_feature as rmpf
import wolframalpha_feature as wf
import wikipedia_feature as wkf
import news_api as nap
import browser_feature as bf
import youtube_feature as yf
import book_api as bap


# changing current working directory
os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S')


# Global list
opening_phrases = ['Welcome Mr. Stark','How May I help U Mr. Stark','Welcome Sir, How may I help You','at your service sir']
exit_when_done = ['thats all jarvis','exit','exit now jarvis','close jarvis','thank you jarvis']

# test function
"""def jarvis_text_opener(text):
    fl = open('J.A.R.V.I.S.txt','w')
    text_list = srtk(text)
    for i in range(0,len(text_list),2):
        fl.write(text_list[i])
        fl.write(text_list[i+1]+'\n')
    fl.close()    
    return
"""
# this function takes recived sentence as an input and returns the task performing word as an output
def task_performing_word(input_sent):
    input_list = wtk(input_sent)
    task_word = ''
    for i in input_list:
        if i == 'book':
            task_word = 'book'
            break
        elif i == 'empty':
            task_word = 'empty'
            break
        elif i == 'lock':
            task_word = 'lock'
            break
        elif i == 'news':
            task_word = 'news'
            break
        elif i == 'open':
            task_word = 'open'
            break
        elif (i== 'search' or i== 'look') and ('wikipedia' in input_list) :
            task_word = 'wikipedia'
            break
        elif i == 'song' or i=='bored':
            task_word = 'song'
            break
        elif i == 'search' and input_list[1] == 'youtube':
            task_word = 'youtube'
            break
        elif i == 'search' or i== 'look':
            task_word = 'browser'
            break
    if task_word == '':
        task_word = 'wolf'
    return task_word


# Waking up JARVIS
def wake_jarvis_up(re_text):
    re_text =re_text.lower()
    text_list = wtk(re_text)
    for i in text_list:
        if i == 'jarvis' or i=='buddy':
            return 'jarvis'
    return

active_check = False
active_text = 'jarvis'

speaker = win32com.client.Dispatch('SAPI.SpVoice')

rs = sr.Recognizer()
with sr.Microphone() as source:
    print("######### CALIBARATING NOISE LEVEL #############")
    rs.adjust_for_ambient_noise(source,duration=float(2))
    # Conversation loop
    while True:
        print("######### CALIBARATING NOISE LEVEL #############")
        rs.adjust_for_ambient_noise(source,duration=float(2))
        if active_check == False:
            print('Speak JARVIS to activate it')
        else:
            print('J.A.R.V.I.S is Listening....')
        audi = rs.listen(source)
        print('Done Recording')

        try:
            print('Sending data to API')
            text_recieved = rs.recognize_google(audi)
            text_recieved = text_recieved.lower()
            print(text_recieved)
            if active_check == False:
                text_recieved = wake_jarvis_up(text_recieved)
            print('Data recieved')
            if text_recieved == 'jarvis':
                active_check = True
                speaker.Speak(ran.choice(opening_phrases))
            elif text_recieved.lower() in exit_when_done:
                speaker.Speak('Exiting Now')
                break
            else:
                finl_task = task_performing_word(text_recieved)
                print(text_recieved)
                if finl_task == 'empty':
                    speaker.Speak('Sure sir')
                    esf.esf.empty_recycle_bin()
                    speaker.Speak('Recycle bin must be empty by now')

                elif finl_task == 'lock':
                    speaker.Speak('locking the laptop screen sir')
                    esf.lock_desktop_screen()

                elif finl_task == 'open':
                    task_value = oaf.give_me_app_name(text_recieved)
                    if task_value == 1:
                        app_n=text_recieved[5:len(text_recieved)]
                        speaker.Speak('opening '+app_n)
                    else:
                        print('Cannot perform task')

                elif finl_task == 'song':
                    rmpf.play_random_music()
                    speaker.Speak('Hope You like the song')

                elif finl_task == 'wolf':
                    answer = wf.wolframalpha_questions(text_recieved)
                    if answer == 0 or answer == 'none':
                        speaker.Speak('I dont know about it Sir')
                    else:
                        speaker.Speak(answer)

                elif finl_task == 'wikipedia':
                    topic = wkf.give_me_topic_name(text_recieved)
                    short_summary = wkf.get_short_summary(topic)
                    print(short_summary)
                    speaker.Speak('showing results on your screen,Sir')
                    

                elif finl_task == 'browser':
                    bf.browser_search(text_recieved)
                    speaker.Speak('Showing search result on the browser sir')

                elif finl_task == 'youtube':
                    yf.open_video_youtube(text_recieved)
                    speaker.Speak('why not sir ')

                
                        
                            
                             
                # Not working properly
                elif finl_task == 'news':
                     news_cat,news_name = nap.give_me_news_name(text_recieved)
                     if news_cat == 'category':
                         nap.get_by_category(news_name)
                     elif news_cat == 'from':
                         nap.get_by_source(news_name)
                     elif news_cat == 'on':
                         nap.get_by_query(news_name)
                     else:
                         speaker.Speak('Sorry, Sir couldn\'t find any relevant news')

        except:
            print('Speak Again sir ')

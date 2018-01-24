""" This module is used for getting information from wikipedia. If user wants some kind of information
    about a particular topic than this module is used.
    """


import wikipedia as wk
from nltk.tokenize import sent_tokenize as stk
from nltk.tokenize import word_tokenize as wtk
import os

# this function takes a user query as an input and returns the topic name which is to be looked for in wikipedia

def give_me_topic_name(user_ask):
    topic = ' '
    user_ask = user_ask.lower()
    user_list = wtk(user_ask)
    user_ask_len = len(user_list)
    i,j = 0,(user_ask_len-1)
    for k in range(0,user_ask_len,1):
        if user_list[k] == 'for':
            i = k+1
        if user_list[k] == 'on' or user_list[k] == 'in':
            j = k-1
    for t in range(i,j+1,1):
        topic = topic+user_list[t]+' '
    topic = topic.strip(' ')
    return topic


    
# This function take a query as an input and returns wikipedia page as an output
def give_wiki_page(query):
    pg = wk.page(query)
    return pg

# This fuction takes query as an input and return a string which is the short summary of that query as an output
def get_short_summary(query):
    os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S')
    fl = open('jarvis_window.txt','w')
    summary = ''
    try:
        wiki_list = stk(wk.summary(query))
        for i in range(0,5,1):
            summary = summary + wiki_list[i]
            print(wiki_list[i],file=fl)
    except wk.exceptions.DisambiguationError:
        summary = 'Sorry Can\'t retrieve data from internet.'
    fl.close()
    os.startfile('jarvis_window.txt')
    return summary

# This function takes query as an input and returns a string which is the long summary of the query as an output.
def get_long_summary(query):
    os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S')
    fl = open('jarvis_window.txt','w')
    summary = ''
    try:
        wiki_list = stk(wk.summary(query))
        for i in range(0,10,1):
            summary = summary + wiki_list[i]
            print(wiki_list[i],file=fl)
    except wk.exceptions.DisambiguationError:
        summary = 'Sorry Can\'t retrieve data from internet.'
    fl.close()
    os.startfile('jarvis_window.txt')
    return summary


# This function returns a image url for a particular query passed to it
def get_page_image(wiki_page):
    img_url =''
    l = len(wiki_page.images)
    if l!=0:
        img_url = wiki_page.images[0]
        return img_url
    return 0

        



    

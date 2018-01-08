""" This module provide interaction between News-Api and J.A.R.V.I.S. It contain various function that can help
    the AI to efficiently provide all the news required by the user.

    Each tuple of a news article has various attributes :-
    1. source
    2. title
    3. description
    4. url
    
    """

import requests as rq
import webbrowser as wb
import os
from nltk.tokenize import word_tokenize as wtk

os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S\\important records')
api_key = '2bc149a1462246949a6e50540a139c3d'
# this function takes a list of tuples as an input and write each in a file

def news_writer(news_list):
    os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S')
    f = open('jarvis_window.txt','w')
    for i in news_list:
        print('\n\nSource    :',i[0],file=f)
        print('Title     :',i[1],file=f)
        print('Author    :',i[2],file=f)
        print('Summary   :',i[3],file=f)
    f.close()
    os.startfile('jarvis_window.txt')
    return
    
# this function takes a query as an input and returns a tuple containing subject and category which help JARVIS to decide which function to call
def give_me_news_name(news_sent):
    news_sent = news_sent.lower()
    news_list = wtk(news_sent)
    
    for i in range(0,len(news_list),1):
        if news_list[i] == 'category':
            return news_list[i],news_list[i-1]

        if news_list[i] == 'from':
            return news_list[i],news_list[i+1]

        if news_list[i] == 'on':
            return news_list[i],news_list[i+1]
    
    return ' '

# this function is used to parse a list
def tuple_genrator(json_obj):
    source_dict = json_obj['source']
    source = source_dict['name']
    author = json_obj['author']
    title = json_obj['title']
    description = json_obj['description']

    return source,author,title,description

# this function takes category string as an input and returns a list of tuple where each tuple contains various attributes of a news article

def get_by_category(category):
    category = category.replace(' ','-')
    base_url = 'https://newsapi.org/v2/top-headlines?category='
    final_url = base_url+category+'&language=en&apiKey='+api_key
    response = rq.get(final_url)
    json_object = response.json()
    totalResults = json_object['totalResults']
    article_list = []
    if totalResults != 0:
        articles = json_object['articles']
        i = 1
        for article in articles:
            if i == 15:
                break
            i +=1
            art = tuple_genrator(article)
            article_list.append(art)
    news_writer(article_list)
    return article_list

# this fuction takes query as an input and returns a list of tuple where each tuple represent an article

def get_by_query(query):
    query = query.replace(' ','%20')
    base_url='https://newsapi.org/v2/top-headlines?q='
    final_url=base_url+query+'&apiKey='+api_key
    response = rq.get(final_url)
    json_object = response.json()
    totalResults = json_object['totalResults']
    article_list = []
    if totalResults != 0:
        articles = json_object['articles']
        i = 1
        for article in articles:
            if i == 15:
                break
            i +=1
            art = tuple_genrator(article)
            article_list.append(art)
    news_writer(article_list)
    return article_list

# this function takes source as an input and returns a list of tuple where each tuple represent a news articel

def get_by_source(source):
    source = source.replace(' ','-')
    base_url = 'https://newsapi.org/v2/top-headlines?sources='
    final_url = base_url+source+'&apiKey='+api_key
    response = rq.get(final_url)
    json_object = response.json()
    totalResults = json_object['totalResults']
    article_list = []
    if totalResults != 0:
        articles = json_object['articles']
        i = 1
        for article in articles:
            if i == 15:
                break
            i +=1
            art = tuple_genrator(article)
            article_list.append(art)
    news_writer(article_list)
    return article_list

#  this function take a url (string as an input) and opens a new webbrowser tab for that url

def open_news_url(news_url):
    wb.open(news_url)
    return

# this funtion takes nothing as an input and return a list containing names of all the favourite source

def list_my_sources():
    f = open('news_api_source_list.txt')
    news = f.read()
    news_list = news.splitlines()
    j = 0
    for i in news_list:
        news_list[j] = i.replace('-',' ')
        j+=1
    f.close()
    return news_list

# this funtion takes nothing as an input and return a list containing names of all the categories
def list_my_category():
    f = open('news_api_category_list.txt')
    news = f.read()
    news_list = news.splitlines()
    j = 0
    for i in news_list:
        news_list[j] = i.replace('-',' ')
        j+=1
    f.close()
    return news_list

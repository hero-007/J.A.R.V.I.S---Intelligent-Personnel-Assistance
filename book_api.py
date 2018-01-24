""" This module provide the functionality of interacting with google books api and respond to
    any type of query made to J.A.R.V.I.S regarding the books ( Which it can handle ).
    Various Functions in the module :-
    1: send_request(query) - direct interaction outside the module
    2: dict_parser(q_dict) - no direct interaction outside the module used inside books_list(json_object)
    3: books_list(json_object) - no direct interaction outside the module used inside send_request(query)
    4: buy_book(buy_link) - direct interaction outside the module
    5: give_me_book_name(book_sent) - direct interaction outside the module 


    Each book has 6 attributes:
    1: book_title
    2: book_author
    3: book_description
    4: book_rating
    5: book_amount
    6: book_buy
    
    """ 

import requests as rq
import webbrowser as wb
from nltk.tokenize import word_tokenize as wtk
import os

# This function takes a list of tuple as an input and write each tuple in a file in a well documented format

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


# This takes a query as an input and extract book name from that query

def give_me_book_name(book_sent):
    book_sent = book_sent.lower()
    word_list = wtk(book_sent)
    book_name = ''
    t = len(word_list)
    
    for i in range(0,t,1):
        if word_list[i]=='book':
            for k in range(i+1,t,1):
                book_name = book_name+word_list[k]
            break
        
    return book_name

# function takes input a query which is a string and it sends request to the api and returns the json object in response

def send_request(book_name):
    base_url = 'https://www.googleapis.com/books/v1/volumes?q='
    book_to_search = book_name.replace(' ','')
    final_url = base_url+book_to_search
    response = rq.get(final_url)
    return (books_list(response.json()))

# function takes dictionary as a input parse it and returns a tuple that contains various information about the book

def dict_parser(q_dict):
    volumeInfo = q_dict['volumeInfo']
    saleInfo = q_dict['saleInfo']
    book_title = volumeInfo['title']
    try:
        book_author = volumeInfo['authors'][0]
    except KeyError:
        book_author = 'Not Mentioned'

    try:
        book_description = volumeInfo['description']
    except KeyError:
        book_description = 'Not Mentioned'

    
    try:
        book_rating = volumeInfo['averageRating']
    except KeyError:
        book_rating = float(0)

    try:
        listPrice = saleInfo['listPrice']
        book_amount = listPrice['amount']
    except KeyError:
        book_amount = float(0)

    try:
        book_buy = saleInfo['buyLink']
    except KeyError:
        book_buy = 'Not Mentioned'

    return book_title,book_author,book_description,book_rating,book_amount,book_buy

# funtion that takes a JSON object as an input and returns a list of tuple where each tuple has information of a particular book

def books_list(json_object):
    books_item_list = []        # Empty book list

    items = json_object['items']

    for item in items:
        book_details = dict_parser(item)                        # tuple containing all the relevant book information
        books_item_list.append(book_details)                    # appending the tupple in a list
    return books_item_list


# function that takes input a buy link if available and open that link in a webbrowser

def buy_book(buy_link):
    wb.open(buy_link)
    return   

# this function takes a a number in words as an input and returns its numeric equivalent

def word_to_num(word):
    if word == 'one':
        return 1
    elif word == 'two':
        return 2
    elif word == 'two':
        return 2
    elif word == 'three':
        return 3
    elif word == 'four':
        return 4
    elif word == 'five':
        return 5
    elif word == 'six':
        return 6
    elif word == 'seven':
        return 7
    elif word == 'eight':
        return 8
    elif word == 'nine':
        return 9
    else:
        return -1
    

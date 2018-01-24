import webbrowser as wb
from nltk.tokenize import word_tokenize as wtk

base_url = 'https://www.youtube.com/results?search_query='

def get_youtube_topic(query_name):
    for_check = False
    topic_search = ''
    query_name = query_name.lower()
    query_name = query_name.strip(' ')
    query_list = wtk(query_name)
    
    for i in range(0,len(query_list),1):
        if query_list[i] == 'for':
            for_check = True
            continue
        if for_check == True:
            topic_search = topic_search + query_list[i]+' '
    return topic_search

def open_video_youtube(query):
    topic_to_search = get_youtube_topic(query)
    final_url = base_url+topic_to_search
    wb.open(final_url)
    return


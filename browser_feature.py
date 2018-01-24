import webbrowser as wb
from nltk.tokenize import word_tokenize as wtk

base_url = 'https://www.google.co.in/search?q='
def browser_search(query):
    search_topic = ''
    for_check = False
    query = query.lower()
    query = query.strip(' ')
    query_list = wtk(query)
    if 'for' in query_list:
        for i in range(0,len(query_list),1):
            if query_list[i] == 'for':
                for_check = True
                continue
            if for_check == True:
                search_topic = search_topic+query_list[i]+' '
    else:
        search_topic = query.replace('search','')
    search_topic = search_topic.strip(' ')
    search_topic.replace(' ','%20')
    final_url = base_url+search_topic
    wb.open(final_url)
    return

            
            
    

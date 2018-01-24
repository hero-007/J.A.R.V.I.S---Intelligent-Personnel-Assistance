""" This module contains a function that use wolframalpha module and use it to find the answer of user's query """

import wolframalpha as wlf

app_id = 'RVW65T-46XEEVG929'
# This function takes a question string as an input and returns a answer string if answer is found else returns 0
def wolframalpha_questions(quest):
    client = wlf.Client(app_id)
    res = client.query(quest)
    answer = ''
    j = 0
    try:
        for i in res['pod']:
            j+=1
            if j == 2:
                final_answer = i['subpod']
                answer=final_answer['plaintext']
    except KeyError:
        return 0
        
    return answer

    

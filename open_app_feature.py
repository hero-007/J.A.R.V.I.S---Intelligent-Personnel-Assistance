""" This module is used to launch a particular application on a system but only those application can be opened whose path is defined inside application_list.txt """
import os


     

# This function takes an app name as an input and open that particular app on the system function returns 1 if the app is opened successfully on the system else it returns 0
def open_app(app_name):
    os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S\\important records')
    f = open('application_list.txt')
    app = f.read()
    app_list = app.splitlines()
    app_dict = {}
    
    for i in app_list:
        app_data = i.split('-')
        app_dict[app_data[0]]=[app_data[1],app_data[2]]
    
    app_name = app_name.lower()
    try:
        os.chdir(app_dict[app_name][0])
        os.startfile(app_dict[app_name][1])
    except KeyError:
        return 0
    return 1
    

# this fuction takes a user query or a user sentence as an input and returns app name which is to be openend
def give_me_app_name(query):
     query = query.lower()
     query = query.strip(' ')
     final_query = query[5:len(query)]
     res = open_app(final_query)
     return res

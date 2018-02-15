import os
os.chdir('C:\\Users\\HP\\Desktop\\J.A.R.V.I.S\\important records')

def validate_user():
    f = open('user_information.txt')
    user = f.read()
    user_data_list = user.splitlines()
    f.close()
    if len(user_data_list) == 0:
        return 0
    else:
        return 1

def new_user():
    

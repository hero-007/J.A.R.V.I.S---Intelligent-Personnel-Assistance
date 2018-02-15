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
    f1 = open('user_information.txt','w')
    f2 = open('application_list.txt','w')

    jarvis_dir = input("Enter the path to J.R.V.I.S directory : ")
    jarvis_dir = jarvis_dir.replace('\\','\\\\')
    print('cwd -',jarvis_dir,file=f1)

    username = input("Enter Your Username : ")
    print('username -',username,file=f1)

    MS_Word = input("Enter the path of MS Word .exe file : ")
    MS_Word = MS_Word.replace('\\','\\\\')
    print('ms word-',MS_Word,file=f2)

    MS_Excel = input("Enter the path of MS Excel .exe file : ")
    MS_Excel = MS_Excel.replace('\\','\\\\')
    print('ms excel-',MS_Excel,file=f2)

    MS_Power = input("Enter the path of MS Power Point .exe file : ")
    MS_Power = MS_Power.replace('\\','\\\\')
    print('ms powerpoint-',MS_Power,file=f2)

    MS_Access = input("Enter the path of MS Access .exe file : ")
    MS_Access = MS_Access.replace('\\','\\\\')
    print('ms access-',MS_Access,file=f2)

    MS_Outlook = input("Enter the path of MS Outlook .exe file : ")
    MS_Outlook = MS_Outlook.replace('\\','\\\\')
    print('ms outlook-',MS_Outlook,file=f2)

    return

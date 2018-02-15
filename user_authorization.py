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
    data_list = []
    jarvis_dir = input("Enter the path to J.R.V.I.S directory : ")
    jarvis_dir = jarvis_dir.replace('\\','\\\\')
    data_list.append(jarvis_dir)
    username = input("Enter Your Username : ")
    data_list.append(username)
    MS_Word = input("Enter the path of MS Word .exe file : ")
    MS_Word = MS_Word.replace('\\','\\\\')
    data_list.append(MS_Word)
    MS_Excel = input("Enter the path of MS Excel .exe file : ")
    MS_Excel = MS_Excel.replace('\\','\\\\')
    data_list.append(MS_Excel)
    MS_Power = input("Enter the path of MS Power Point .exe file : ")
    MS_Power = MS_Power.replace('\\','\\\\')
    data_list.append(MS_Power)
    MS_Access = input("Enter the path of MS Access .exe file : ")
    MS_Access = MS_Access.replace('\\','\\\\')
    data_list.append(MS_Access)
    MS_Outlook = input("Enter the path of MS Outlook .exe file : ")
    MS_Outlook = MS_Outlook.replace('\\','\\\\')
    data_list.append(MS_Outlook)

    f = open('user_information.txt','w')
    for i in data_list:
        print(i,file=f)
    f.close()
    return
    

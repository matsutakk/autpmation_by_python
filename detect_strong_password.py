import re
import pyperclip

def detection(password):
    flag=1
    strong_password = re.compile(r'''
                                        [a-zA-z\d]{8,}
                                ''',re.VERBOSE)
    if(strong_password.search(password)==None):
        print("Your password is too short. At least 8 length.")
        flag=0
        
    strong_password = re.compile(r'''
                                        ^(?=.*?[a-z])
                                ''',re.VERBOSE)
    if(strong_password.search(password)==None):
        print("You should add at least one Lowercase.")
        flag=0
    
    strong_password = re.compile(r'''
                                    (?=.*?[A-Z])
                                    ''',re.VERBOSE)
    if(strong_password.search(password)==None):
        print("You should add at least one Uppercase.")
        flag=0
    
    strong_password = re.compile(r'''
                                    (?=.*?\d)
                                ''',re.VERBOSE)
    if(strong_password.search(password)==None):
        print("You should add at least one number.")
        flag=0
        
    if(flag):
        print("Your password is strong")

detection(str(pyperclip.paste()))
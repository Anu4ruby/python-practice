#regex basics
#https://www.w3schools.com/python/python_regex.asp
import re

#using regex
def email_validation(s):
    if re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[A-Za-z]{2,}$",s):
        print("email is valid")
    else:
        print("email is not valid")

s = input("enter your email:")
#email_validation(s)

#using string functions
def string_email_validation(s):
    at_index = s.find('@')
    dot_index = s.find('.')

    #check if there is no two consecutive dots or ats
    if(('@' and '.' in s) and s[at_index+1] != '@' and s[dot_index+1] != '.'):

        #domain name should be in allowed list
        if(s[-3:] in ('com','in','gov','edu','uk','org')):
            #can start with alphabets, numbers or allowed special characters
            if(s[0].isalnum() or s[0] in ('-','_')):
                print("email is valid")
            else:
                print("email not valid")
        else:
            print("email not valid")
    else:
        print("email not valid")

string_email_validation(s)

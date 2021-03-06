#WRITTEN BY: ALI ALNUAIMI ~ https://www.linkedin.com/in/ali-alnuaimi-9847a1164/

#OBJECTIVE
    #Brute force password protected word documents 
    
#USAGE:
    #1- CMD: Enter the folder where this script is located
    #2- CMD: Type "word_bruteforce.py" and follow the instructions

#REQUIREMENTS: Below libraries to be installed "pip install <lib_name>"

#NOTES: FOR EDUCATION PURPOSES ONLY

import tempfile, shutil, os
import random
from win32com.client import Dispatch



def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, str(random.randint(1, 100000)) + 'temp_file_name.docx')
    shutil.copy2(path, temp_path)
    return temp_path

def find_word_password(file, password_list):
    print ("Starting ...")

    instance = Dispatch('Word.Application')
    temp_file = create_temporary_copy(file)

    for pw in password_list:
        try:
            print("Attempting: " + pw.strip())
            instance.Documents.Open(temp_file, False, True, None, pw.strip())
            print ("Password Found!: " + pw.strip())
            print ("Stopping...")
            break
        except:
            pass
    try:
        instance.Documents.Close(SaveChanges = 0)
    except:
        pass
    instance.Quit()

    os.remove(temp_file)




if __name__ == '__main__':

    file = ""
    password_list = []

    while True:
        input1 = input('File to bruteforce (.docx): ')
        if (input1.split(".")[-1] == "docx" and os.path.exists(input1)):
            file = input1
            break
        else:
            print ("File type not supported or file doesn't exist")


    while True:
        input2 = input('Wordlist (.txt): ')
        if (input2.split(".")[-1] == "txt" and os.path.exists(input2)):
            password_list = open(input2,'r').read().splitlines()
            break
        else:
            print ("File type not supported or file doesn't exist")


    find_password(file, password_list)

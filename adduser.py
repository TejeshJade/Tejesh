import os

def newUser():
    confirm = "N"
    while confirm != "Y" :
        username = input("Enter the name of the user to add: ")
        print("Use the username '" + username + "'? (Y/N)")
        confirm = input().upper()
        if confirm == "Y" :
            print("code sucessfully run")
        else:
            print("no")
            
    os.system("sudo adduser " + username)
newUser()

from cryptography.fernet import Fernet
import os
import time
###################################### Create a key #######################################
def createKey():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open("key.key", "wb") as file:
            file.write(key)
        return 
#display all the accounts + psws
def Display():
    key = createKey() 
    crypting = Fernet(key)
    while(True):
        i=1
        os.system('cls')
        try:
            with open("passwords.txt","r")as file:
                file.readline()
                for line in file:
                    words=line.split()
                    print(str(i)+" : "+words[0]+" "+crypting.decrypt(words[1].encode()).decode())#,end=""
                    i+=1
                back=input("Back to menu(1=yes)")
                if back=="1":
                    break
                #os.system('cls')
                #print("bakc")
                else:
                    continue
        except Exception as exception: 
            print(exception)
            time.sleep(3)
        
#Adding a new account + psw
def Add():
    key=createKey()
    crypting=Fernet(key)
    os.system("cls")
    account=input("Enter account name :")
    psw=input("Enter password :")
    with open("passwords.txt","a")as file:
        file.write(account+" "+crypting.encrypt(psw.encode()).decode()+"\n")

#Deleting account + it's psw
def Delete():
    os.system('cls')
    number=int(input("Enter number of line of password you want to delete :"))
    with open("passwords.txt","r")as file:
        lines=file.readlines()
        if number<1 or number>len(lines):
            print("Wrong number")
            time.sleep(3)
        else:
            lines.pop(number)
            with open("passwords.txt","w")as file:
                file.writelines(lines)
                
#update psw
def Update():
    key=createKey()
    crypting=Fernet(key)
    os.system('cls')
    number=int(input("Witch password you want to update (number) :"))
    with open("passwords.txt","r")as file:
        lines=file.readlines()
        if number<1:
            print("Wrong number !")
        else:
            try:
                words=lines[number].split()
                newpsw=input("Enter the new password :")
                lines[number]=lines[number].replace(words[1],crypting.encrypt(newpsw.encode()).decode())
                with open("passwords.txt","w")as file:
                    file.writelines(lines)
            except IndexError as error:
                print("This line doesn't exist !!!")
                time.sleep(3)#wait 3 seconds then display the menu
    #print("Updated")
#Menu
def Menu():
    print("*Welcome to psw manager*")
    #print("Menu")
    while(True):
        os.system('cls')
        print("1_Display my passwords .")
        print("2_Add new password .")
        print("3_Delete a password .")
        print("4_Update a password .")
        print("5_LogOut .")
        choice=int(input("What do you want to do :"))
        if choice==1:
            #os.system('cls')
            Display()
        elif choice==2:
            #os.system('cls')
            Add()
        elif choice==3:
            #os.system('cls')
            Delete()
        elif choice==4:
            #os.system('cls')
            Update()
        elif choice==5:
            os.system('cls')
            print("LogOut successed :)")
            break
#Main
import os
os.system('cls')
print("****************************************Welcome to psw manager****************************************")
masterPsw=input("Enter your master password :")
#print(masterPsw)
try:
    with open("passwords.txt","x")as file:
        file.write(masterPsw+"\n")
        print("password written:)")
        os.system('cls')
    Menu()
    #file.close()
except FileExistsError as e:
    with open("passwords.txt","r")as file:
        if(file.readline().strip()==masterPsw):#strip to remove whitespaces and new line
            print("login:)")
            os.system('cls')
            Menu()
        else:
            print("Wrong password :(")

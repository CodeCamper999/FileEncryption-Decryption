# github https://github.com/CodeCamper999
# DO NOT ENCRYPT RTF FILE PLEASE CHECK README ON HOW TO CHANGE FORMAT OF FILE ON MAC
# IF YOU DECIDE TO ENCRYPT A RTF YOU WILL NOT BE ABLE TO DECRYPT IT!
from cryptography.fernet import Fernet
import os

print(" Please see README on github for help ")
help = """
In order to go to the file you want to encrypt you need to know how to 
go to the dir(directory) see this example:
/users/cookies/documents/file.txt
"""

key = Fernet.generate_key()
f = Fernet(key.decode("utf-8"))

with open("DecryptionKey.txt", "wb") as GetKey:
    
    GetKey.write(key)

RunAgain = True

def EncryptData():
    RunAgain = True
    while RunAgain == True:
        GetFile = input("Please enter the file you would like to encrypt(-H for help or input D to skip to decryption: press e to exit): ")
        IfFile = os.path.isfile(GetFile)
        if GetFile in ("-H", "-h"):
            print("help")
        elif GetFile in ("e", "E"):
            exit()
        if IfFile == True:
            
            with open(GetFile, "rb") as UsrFile:
                ReadFile = UsrFile.readline()
                
            encryptdata = f.encrypt(ReadFile)
            print("File has been encrypted")
            
            with open(GetFile, "wb") as OverWrite:
                OverWrite.write(encryptdata)
        elif IfFile == False:
            print("That file is not found(Please contact me in SOCIALS or check README for help)")
            exit()
        print("In order to decrypt files please have key and input D to skip to decryption")
        QuitLoop = input("Would you like to stop encrypting Files?[Y:Press enter to decrypt]: ")
        
        if QuitLoop in ("Y", "y",):
            print("Now stoping...")
            exit()
        
            
        with open("DecryptionKey.txt", "r") as SeekKey:
            
                    
            Getline = SeekKey.readlines()
                    
            
            TrueKey = ", ".join(Getline)
                        
        FileDecrypt = input("Please enter the file you would like to decrypt?: ")
        IsFile = os.path.isfile(FileDecrypt)
        
        
        
        if IsFile == True:
            with open(FileDecrypt, "rb") as DecryptFile:
                GetFile = DecryptFile.read()
            GetkeyUsr = input("What is the decryption key?: ")
            if GetkeyUsr == TrueKey:
                Decryptionkey = f.decrypt(encryptdata)
                
                with open(FileDecrypt, "wb") as ReadFile:
                    ReadFile.write(Decryptionkey)
                    print("File has been decrypted")
            elif GetkeyUsr != TrueKey:
                print("Not Correct Key")
        elif IsFile == False:
            print("No Such Directory Please visit README on github")
        else:
            print("nothing was selected exiting...")
            exit()           
            
EncryptData()




        
    
       
    

    
    





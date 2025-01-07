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

key = Fernet.generate_key() # Generates key in bytes
f = Fernet(key.decode("utf-8")) # In order to decrypt the file we need to decode the bytes 

with open("DecryptionKey.txt", "wb") as GetKey: # opening File and writing the key in the file 
    
    GetKey.write(key)
    # using "wb" allows us to write binary because once again key is in bytes not a str 
RunAgain = True
# Allow user to stop running while loop 

def EncryptData(): # Created a function called Encrypt Data 
    RunAgain = True
    while RunAgain == True: 
        GetFile = input("Please enter the file you would like to encrypt(-H for help or input D to skip to decryption: press e to exit): ")
        IfFile = os.path.isfile(GetFile) 
        # using os to get the path of a file nd finding out if it is a file using .isfile() which would give us a boolean(true or false) value
        if GetFile in ("-H", "-h"):
            print("help")
        elif GetFile in ("e", "E"):
            exit()
        if IfFile == True:
            # if the file exist then we will run this code
            with open(GetFile, "rb") as UsrFile:
                ReadFile = UsrFile.read()
                # Reads the entire text inside the fle 
            encryptdata = f.encrypt(ReadFile)
            # we got the key(f) and encrpyted the file the user choose 
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
        
        RangeOfNUm = list(range(1))    
        # we created a list using list and used range to get range through a number 
        with open("DecryptionKey.txt", "r") as SeekKey:
            
                    
            Getline = SeekKey.readlines()
            # We are reading the Decryptionkey file by line 1
                    
            TrueKey = ", ".join(Getline)
            # we are trying to remove the bracets and any other things that are not the key
            # so we used join() method
        FileDecrypt = input("Please enter the file you would like to decrypt?: ")
        IsFile = os.path.isfile(FileDecrypt)
        # Checking if the user put in a file that exist
        
        
        
        if IsFile == True:
            with open(FileDecrypt, "rb") as DecryptFile:
                GetFile = DecryptFile.read()
            GetkeyUsr = input("What is the decryption key?: ")
            if GetkeyUsr == TrueKey:
                # If the key the user put in and it's in the Decryptionkey.txt file then execute this
                Decryptionkey = f.decrypt(encryptdata)
                # we are getting the key using "f" we are decrypting the file using decrypt() and we put the variable that encrypted the file to start 
                
                with open(FileDecrypt, "wb") as ReadFile:
                    ReadFile.write(Decryptionkey)
                    # We are writing the txt that was previously put inside the txt file 
                    print("File has been decrypted")
            elif GetkeyUsr != TrueKey:
                # If the key the user put in is not inside the DecryptionKey file then run this code:
                print("Not Correct Key")
        elif IsFile == False:
            # If file doesn't exist 
            print("No Such Directory Please visit README on github")
        else:
            print("nothing was selected exiting...")
            exit()           
            
EncryptData()




        
    
       
    

    
    





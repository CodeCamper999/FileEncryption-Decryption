# FileEncryption-Decryption
I will explain and show you how you can encrypt and decrypt your files using cryptography 

Q:A

Questions:

When I run the file it says file cannot be found, what do I do?

Answer:

In order to go into directories you need to do /users/(yourcomputername)/documents/file.txt

---

Qestion:

I can't open my encrypted file on mac 

Answer:

In order to open and write to a file it needs to be in a txt format, ofc you can still write to a rtf file
but then the problem will come in where you cannot open the rtf file because it's in a different format, there's no way inside this code where you can decrypt it even if it says the file has been decrypted... In order to change a rtf into a txt file you can go to TextEdit > Format > Make Plain Test.
You can find format on the top bar because the apple sign. 
----
Questions:

I can't find decrpytionkey.txt file after using python in terminal 

Answer:

python will open/create a file where the user chooses, in my code I created a open function to create/read/write a file where the code is being ran meaning if you run the file inside your terminal/cmd the file would be inside the terminal/cmd directory you can fix this by change where the file is being created example:
This line can be found on line 17-20 

with open("/users/hellscapelove/documents/DecryptionKey.txt", "wb") as GetKey:
    GetKey.write(key)

personally I would want to put a directory that is deep inside other direectories so the file key would be harder to spot with a different name that is not Decryptionkey example:

with open("/users/hellscapelove/documents/songs.txt", "wb") as GetKey:
    GetKey.write(key)
    
----








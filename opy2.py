#creating a new file
new_file=open("new_File.txt")
new_file.close()

#Check if a file exist 

import os
print("Cecking if my file exists or not........\n")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

#create a new file if it doesn't
my_file=open("my_file.txt","w")
my_file.write("Hi i am learning phyton and file handling.")
my_file.close()

os.remove("Codingal (1).txt")
os.rmdir('Folder')
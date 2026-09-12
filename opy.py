#using with funtion
with open ("Codingal (1).txt","w")as file:
     file.write("\nHi welcome to codingal\n")
file.close()
#Spilt file into words 

with open("Codingal (1).txt","r")as file:
    data =file.readlines()
    print("Words in this file are.....")
    for line in data:
         word =line.split()
         print(word)
file.close()

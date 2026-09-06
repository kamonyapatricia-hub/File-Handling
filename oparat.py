#Open File in Read Mode

file_read=open ("Codingal (1).txt","r")
print("File in Read Mode")
print(file_read.read())
file_read.close()


#Open file in write mode 
our_file =open ("Codingal (1).txt","w")
#writing in the file 
our_file.write("This is file in write mode...")
our_file.write("Today we have Pharell and Hannie in class,")
our_file.write("They are learning about operations on a file.")
our_file.close()

#open the file in append mode 

file_append =open("Codingal (1).txt","a")
#Appending the file 
file_append.write("\n File in append Mode...")
file_append.write("\n Appending means adding another text at the end of the file.")
file_append.close()

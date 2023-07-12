random = open("file.txt", "r")#------> only read the data 
#open("file.txt", "w")#------> write in  the data
#open("file.txt", "a")#------> change or add the data in the file 
#open("file.txt", "r+")#------> read and write the data the data in the file 
print(random.readable())#------> to check weather we can read the file or not 
print(random.read())#-----> split out all the information 
print(random.readline())#-----> specifically read a single line 
print(random.readlines())#----> this function simply put all the information in a single list 
random.close()

# we can also do it with the help of for loop like:
for abc in random.readlines():
    print(abc)
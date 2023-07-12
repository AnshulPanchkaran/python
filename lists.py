
# a list is used to store the data 
# is starts from [] braces 
#it is mutable means changeble 
# it allows duplicates


luckey_number=[4,5,6,9,7,10]
friends = ["ram","anshul","sham","abc","cde"]
#friends[1]="bcv"
#print(friends[1:3])

#friends.extend(luckey_number)-------> to put list in another list

#friends.append("cbv")  ---------->at the end add the number at end 

#friends.insert(1,"rohit") --------->to insert an element at the index position or at the end direct if no index is given 

#friends.remove("abc")-------> to remove an element 

#friends.pop()---------> remove the last element

#friends.clear()----------->to clear the full list

#print(friends.index("anshul"))------->at what position the word or string start 

#print(friends.count("anshul"))--------->to count te element in string 

#print(friends.sort()) ------> to sort the list in assending order according to ascii

#print(friends.sort(reverse=True))---------> to sort list in ascending order


#luckey_number.reverse()----------> to reverse the list

#print(luckey_number)

#print(friends)

friends2=friends.copy()# -------> to copy the 1 list into another list

print(friends2)
is_male = True
is_tall = False

'''if is_male or is_tall:
    print("you are a male or tall guy")
else:                                                   if one is true the true and both false then only false 
    print("you are neither  a male nor tall ")'''

if is_male and is_tall:
    print("you are a tall male ")
elif is_male and not (is_tall):
    print(" you are a short male ")
elif not(is_male) and  is_tall:
    print(" you are not  male  but you are tall ")
else:                                                    #if one is flase then false both should be true 
    print("you are not a male or not tall  ")

# it allow us to store diffrent values or informations or key value pair 
# it is reffered through key when we want to access any value or information 
# it always start with {} braces 
# the word is what like uniqually identifies it insude of distionaries and then the value would be actuall defination



month_conversuion = {
    "jan" : " january ",
    "feb" : " feburary ",
    "mar": " march",
    "apr": " april",
    "may ": " may ",
    "jun": " june ",
    "jul": " july",
    "aug":" august",
    "sep": " september",
    "oct": " octuber",
    "nov": " november ",
    "dec": " december ",
}


print(month_conversuion["jan"])
print(month_conversuion.get("luv", " not valid "))
print(month_conversuion.get(input("enter the month")))
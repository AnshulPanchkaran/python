secert_word = "anshul"
guess = ""
guess_count = 0
guess_limit =3
out_of_guess= False
print(" you have three chances to guess the word ")
while guess != secert_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess=input(" enter the guess word: ")
        guess_count += 1
        if guess != secert_word:
            print(" you guess wrong ")
    else:
        out_of_guess = True

if out_of_guess:
    print(" you lose.... your three chances are done ")
else:    
    print(" you win!.... congo!!!")

  
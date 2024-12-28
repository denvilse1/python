import random

name=input("What's your name")
print("Good luck !", name)

words=['cars','computer','python','Django','frontend','data','Artificial Engineer']
word=random.choice(words)

print("Guess the character")

guesses=''
turns=12

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end="+")
        
        else:
            print("_", end=' ')
            failed+=1
    if failed == 0:
        print()
        print("you win")
        print("The word is : ",word)
        break
    print()

    guess=input("guess the character")
    guesses+=guess

    if guess not in word:
        turns-=1
        print("wrong")
        print("You have ",+ turns,'more guesses')

        if turns==0:
            print("you loose")
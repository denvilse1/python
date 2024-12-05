import random
print("Welcome to number guessing game using python")

g_counter=0
chances=5
number_to_guess=random.randrange(100)
print(number_to_guess)

while(g_counter<=chances):
    g_counter+=1
    my_guess=int(input("Enter your guess"))

    if my_guess==number_to_guess:
        print(f"Congrats you have guessed the number : {number_to_guess} correct, in {g_counter} chances ")
        break
     
    elif(g_counter>=chances and my_guess!=number_to_guess):
        print(f"Your guess {my_guess} is not  the number to guess as the number is :{number_to_guess}")
        

    elif my_guess>number_to_guess:
        print("Your is higher than the number")
    else:
        print("Your guess the number lesser then the number to guess")
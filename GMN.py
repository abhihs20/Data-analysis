# Game Criteria
# 1. Starts by generating a Random number b/w 1-20
# 2. user has to Guess the SecretNumber
# 3. UG > SN (Too High)
# 4. UG < SN (Too LOw)
# 5. UG == SN (Correct GUess)

import random

# random : it's a Module which is used to generate the random number or random entities

secretNumber = random.randint(1,20)
print(secretNumber)
score=20
# Taking user Input

while True:

    
    
    userGuess = int(input("Enter the Guess.:  "))

    if(userGuess == secretNumber):
        print("Correct Guess 🎉")
        print(f" your score is {score}")
        break

    elif(userGuess > secretNumber):
        print("Too High")
        score-=1

    else:
        print("Too Low")
        score-=1
        
        

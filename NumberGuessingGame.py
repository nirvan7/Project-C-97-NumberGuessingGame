import random;

print("Number Guessing Game")
print("Guess a Number in Between 1 and 9")
number = random.randint(1,9)
for i in range(5):
   
    guess=int(input("Enter Your Guess"))
    if guess==number:
        print("Congratulations You Won")
        break
    elif guess<number:
        if i<4:
         print("Your Guess Was Too Low, Guess A Higher Number Than",guess)
        else:
         print("You Lose") 
    else:
        if i<4:
         print("Your Number Is Too High, Please Select A Lesser Number Than",guess)
        else:
         print("You Lose") 
   
        
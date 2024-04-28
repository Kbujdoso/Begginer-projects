import random

def number(x):
    z = random.randint(1, x)
    return z 
    

x = int(input("The range you want to play in: "))
y = int(input("Your guess: "))
z = number(x)
k = 1
while y != z:
    if y > z:
        print("Too high")
    else: 
        print("Too low!")
    y = int(input("Your new guess: "))
    k += 1

print(f"You won the correct number was {y}! You guessed it correctly form {k} guesses!") 


import random
print(" L = Low H = High C = correct")
y = int(input("In which range is your number? (1 ,10 ,100, 1000... etc.)"))
x = 1
def number(x , y):
    return random.randint(x, y)

z = number(x, y)  
answer = ""
while answer != "C":
        print(f"This is your number: {z}?")
        answer = input("High low or correct?: ")
        if answer == "L":
            y = z-1
        elif answer == "H": 
            x = z+1
        z = number(x , y)

print(f"The correct number was {z}")
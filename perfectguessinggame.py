import random
print(" L = Low H = High C = correct")
y = int(input("In which range is your number? (1 ,10 ,100, 1000... etc.)"))
def perfect(k):
    return round(y/2**k)
k = 1
z = perfect(k)

answer = ""
while answer != "C":
    print(f"This is your number: {z}?")
    answer = input("High low or correct?: ")
    k += 1
    if answer == "L": 
        z -= perfect(k)
    elif answer == "H":
        z += perfect(k)
print(f"The correct number was {z}")



















































"""z = number(x, y)  
answer = ""
while answer != "C":
        print(f"This is your number: {z}?")
        answer = input("High low or correct?: ")
        if answer == "L":
            y = z-1
        elif answer == "H": 
            x = z+1
        z = number(x , y)

print(f"The correct number was {z}")"""
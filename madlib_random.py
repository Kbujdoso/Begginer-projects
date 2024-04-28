"""import madlib1
import madlib2
import madlib3
import random 
list1 = [madlib1.madlib10(),madlib2.madlib11(), madlib3.madlib13()]
a = random.choice(list1)
a"""
import madlib1
import Madlib.madlib2 as madlib2
import Madlib.madlib3 as madlib3
import random 

list1 = [madlib1.madlib10, madlib2.madlib11, madlib3.madlib13]  # Note: Removed the function call parentheses
selected_madlib = random.choice(list1)()  # Call the selected function to get the madlib
print(selected_madlib)
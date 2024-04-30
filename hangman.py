import random
from hangman_words import words
def good_word(words):
    word = random.choice(words)
    while " " in word or "-" in word: 
        word = random.choice(words)
    return word 
word = good_word(words)
correct_letters = []
guessed_letters = []
current_word= ""
print(word)
y = 0
def letters(x): 
    global y 
    if x in set(word): 
        correct_letters.append(x)
        guessed_letters.append(x)
    else: 
        guessed_letters.append(x)
        y = y + 1 
    return correct_letters , guessed_letters 
def shown_word(word):
    current_word = ""
    for i in range(len(word)):
        if word[i] in correct_letters: 
            current_word = current_word + word[i]
        else: 
            current_word = current_word + "-"
    return current_word

while "-" in shown_word(word) and y != 11:
    letter = input("Guess a letter!: ")
    letters(letter)
    print(shown_word(word))
    print(guessed_letters)
if y == 11: 
    print("You lost!")
else: 
    print(f"You won the world was {current_word}")


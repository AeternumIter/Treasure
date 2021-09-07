import time
import sys
correctanswers = 0
incorrect = 0

def fail():
    if incorrect >= 3:
        sys.exit("YOU FAILED")

    

print("In this puzzle you have to figure out what tech company i'm talking about. in each question")
time.sleep(5)
print("You get 3 guesses with each question")
time.sleep(1)
print("There are 5 questions total")
time.sleep(2)
print("The Question Is:")
print("The tech company ROG (Republic of Gamers) is a sub-brand of what major tech company?")
answer = input("")
if answer == "ASUS" or "asus" or "Asus":
    print("That's Correct!")
    correctanswers+=1
else:
    print("I'm sorry, it was ASUS")
    incorrect+=1
fail()

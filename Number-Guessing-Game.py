# Number Guessing Game

from random import randint
flag = False
count = 0
CorrectNumber = randint(1,250)
print("Guess the Correct Number From 1-250")
print("You have 10 Tries")
GuessNumber = input("Lets Begin , Input the first number : ")
while not flag and count < 9:
    try:
        guess_number = int(GuessNumber)
    except ValueError:
        print("Please enter a valid number.")
        GuessNumber = input(f"Input the, number : ")
        continue
    if int(GuessNumber) < 1 or int(GuessNumber) > 250:
        print("Out of range! Please guess a number between 1 and 250.")
        GuessNumber = input(f"Input the number : ")
        continue
    count += 1
    if int(GuessNumber) == CorrectNumber:
        print("Wow,Congratulations You guessed the number in ",count, "tries")
        flag = True
    elif int(GuessNumber) > CorrectNumber:
        print("Too high")
        flag = False
    elif int(GuessNumber) < CorrectNumber:
        print("Too Low")
        flag = False

    GuessNumber = input( f"Input the, {count+1} , number : ")

if not flag:
    print(f"Sorry, you've used all your tries. The correct number was {CorrectNumber}.")


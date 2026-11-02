secret_number = 7

guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("Congratulations! Correct Guess!")

elif guess < secret_number:
    print("Your number is too small!")

else:
    print("Your number is too big!")
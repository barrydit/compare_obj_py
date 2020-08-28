num = [2,4,6,8,10]

while True :
    n = input("Guess a number or press \"q\" to quit: ")
    if n == "q":
        break
    else:
        n = int(n)
        if n in num:
            print("You guessed correctly.")
        else:
            print("Wrong guess.")
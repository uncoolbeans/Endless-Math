#Endless math game

import random

def convert_Input_To_Int():
    while True:
        x = input("Enter your selection: ")
        try:
            x = int(x)
            break
        except ValueError:
            print("Invalid input. Try again.")
    return x

def answerRecieve():
    while True:
        ans = input("Enter your answer: ")
        try:
            ans = int(ans)
            break
        except ValueError:
            print("Invalid input. Try again.")
    return ans

def questions(x,negativenums):
    print("How big do you want values to be?")
    numRange = convert_Input_To_Int()
    points = 0
    while True:
        if negativenums:
            a = random.randint(-numRange,numRange)
            b = random.randint(-numRange,numRange)
        else:
            a = random.randint(0,numRange)
            b = random.randint(1,numRange)
        if x == 1:
            c = a + b
            print(f"{a} + {b} = ? ")
        elif x == 2:
            c = a - b
            print(f"{a} - {b} = ? ")
        elif x == 3:
            c = a * b
            print(f"{a} x {b} = ? ")
        elif x == 4:
            while True:
                c = a/b
                if a%b != 0:
                        if negativenums:
                            a = random.randint(-numRange,numRange)
                            b = random.randint(-numRange,numRange)
                        else:
                            a = random.randint(0,numRange)
                            b = random.randint(1,numRange)
                else:
                    print(f"{a} / {b} = ? ")
                    break
            print(f"{a} / {b} = ? ")
        elif x == 5:
            operatorchoose = random.randint(1,4)
            if operatorchoose == 1:
                c = a + b
                print(f"{a} + {b} = ? ")
            elif operatorchoose == 2:
                c = a - b
                print(f"{a} - {b} = ? ")
            elif operatorchoose == 3:
                c = a * b
                print(f"{a} x {b} = ? ")
            elif operatorchoose == 4:
                while True:
                    c = a/b
                    if a%b != 0:
                        if negativenums:
                            a = random.randint(-numRange,numRange)
                            b = random.randint(-numRange,numRange)
                        else:
                            a = random.randint(0,numRange)
                            b = random.randint(1,numRange)
                    else:
                        print(f"{a} / {b} = ? ")
                        break
        answer = answerRecieve()
        if answer == c:
            print("Correct!")
            points += 1
        else:
            print(f"Incorrect! You got {points} questions correct.")
            break

def negnumtoggle():
    posneg = input("""Enable negative numbers? They will have the same magnitude as the number range entered.
    (y/n) """)
    if posneg == "y":
        return True
    elif posneg == "n":
        return False

def restart():
    while True: 
        restart = input("Restart game? (y/n)")
        if restart == "y":
            return True
            break
        elif restart == "n":
            return False
            break
        else:
            print("Invalid input. Re-enter.")

def Main():
    print("""Enter 1 for Addition
Enter 2 for Subtraction
Enter 3 for Multiplication
Enter 4 for Division
Enter 5 for all""")
    play = True
    while play:
        optype = convert_Input_To_Int()
        posneg = negnumtoggle()
        if optype == 1:
            print("Addition chosen...")
            questions(optype,posneg)
            break
        elif optype == 2:
            print("Subtraction chosen...")
            questions(optype,posneg)
            break
        elif optype == 3:
            print("Multiplication chosen...")
            questions(optype,posneg)
            break
        elif optype == 4:
            print("Division chosen...")
            questions(optype,posneg)
            break
        elif optype == 5:
            print("Mixed chosen...")
            questions(optype,posneg)
            break
        else:
            print("Invalid input. Please re-enter.")
        play = restart()

Main()
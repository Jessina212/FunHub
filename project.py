import random
from datetime import datetime
import sys
import cowsay
import time


def ran_generator():
    num = random.randint(1000, 9999)
    return num


def check(user_num, num):
    if user_num != num:
        return True  # we want while loop to continue till the number doesn't match
    return False


def match(user_num, num):
    user_num = str(user_num)
    num = str(num)

    n = 0

    for i in range(0, 4):
        if user_num[i] == num[i]:
            n += 1

    return n


def alert(LIMIT, start_time):
    elapsed = (datetime.now()-start_time).total_seconds()
    remaining = LIMIT-elapsed
    alert_30 = False

    if remaining <= 0:
        return 0
    elif remaining <= 10:
        return f"{int(remaining)} seconds left"
    elif remaining <= 30 and not alert_30:
        alert_30 = True
        return f"{int(remaining)} seconds left"

def greet():
    animals = cowsay.char_names
    animal = random.choice(animals)

    return(cowsay.get_output_string(animal, "Start Guessing!"))

def play_again():
    time.sleep(2)

    while True:
        print("What would you like to do?")
        print("1. Play Again")
        print("2. Play another game")
        print("3. Exit")

        try:
            ans = int(input("Enter 1, 2 or 3: "))
        except Exception:
            ans = int(input("Please choose a valid option."))

        if ans==1:
            return "again"
        elif ans ==2:
            return "menu"
        else:
            return "exit"


def main():
    #color scheme for logo
    FUN = "\033[1;38;2;33;83;196m"
    HUB = "\033[1;38;2;66;151;168m"
    RESET = "\033[0m"

    print(f"Welcome to {FUN}Fun{HUB}Hub{RESET}- Where fun is INFINITE and \033[1;4mnever ends\033[0m")
    time.sleep(1) #waiting for 1 second before the other print statement
    print("What are you waiting for??? Start having unlimited fun")

    option = None
    while True:
        if option is None:
            try:
                #color and bold, underline formatting
                print("Choose a game- \033[1mNumGuesser\033[0m[1] (for \033[4molder human species\033[0m) or \033[1mAnimalTalk\033[0m[2] (for \033[4mkidlings\033[0m)")
                option = int(input())
            except Exception:
                option = int(input("Please choose one fo the options from the above list: "))

        if option==1:

            num = ran_generator()
            print("I have selected a number, now it's your turn to guess. Good Luck!")
            time.sleep(1)
            print("2 minute timer starts now.")
            print(greet())
            count = 0
            start_time = datetime.now()
            TIME_LIMIT = 120
            won = False

            try:
                user_num = int(input())
                while check(user_num, num):
                    # Timer Logic
                    a = alert(TIME_LIMIT, start_time)


                    if a == 0:
                        print(f"Time's Up!! You Lost!")
                        print(f"The number was {num}")
                        won= False
                        break
                    elif a:
                        print(a)

                    #Number of Turns Logic
                    if count >= 20:
                        print(f"You Lost! The number was {num}")
                        wont=False
                        break

                    if match(user_num, num) != 0:
                        print(f"{match(user_num, num)} digits are in the right spot!")
                    else:
                        print("No digits are in the right spot.")
                    user_num = int(input())
                    # continue input till the number input is not a 4 digit number
                    while user_num > 9999 or user_num < 1000:
                        print(f"Please enter a valid 4 digit integer.")
                        user_num = int(input())

                    count += 1
                else:
                    won = True

            except Exception:
                print("Please input a valid 4 digit number.")
                user_num = int(input())

            if won:
                end_time = datetime.now()

                time_taken = end_time - start_time

                print(f"You WON finally!!, YES the number was {num}, phew, it just took about {count} tries. Here is your statistics: ")
                print(f"Number of tries: {count}")
                print(f"Time Taken: {int(time_taken.total_seconds())} seconds")

        elif option ==2:
            print(",".join(cowsay.char_names))

            a=input("Choose your character from the above list: ")
            while a.lower() not in cowsay.char_names:
                a = input("Choose your character: ")
            b = input("What do you want it to say? ")

            print(cowsay.get_output_string(a.lower(), b))

        choice = play_again()
        if choice=="exit":
            print("Thanks for playing!! See you next time!")
            break
        elif choice == "menu":
            option = None

    return 0


if __name__ == "__main__":
    main()

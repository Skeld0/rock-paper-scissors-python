import random

def rps_game():
    user_win = 0
    computer_win = 0
    options = ["R", "P", "S"]
    R = "R" 
    P = "P"
    S = "S"
    print("Welcome to the Rock-Paper-Scissors game. You will play with computer for 3 wins. ")
    while user_win<3 and computer_win<3:
        user_choice = input(f"Your choise is? Choose only one of three({R}, {P} or {S}) ")
        computer_choice = random.choice(options)
        if user_choice == R and computer_choice == S or user_choice == S and computer_choice == P or user_choice == P and computer_choice == R:
            print("You won! ")
            user_win += 1
        elif user_choice == computer_choice:
            print("Draw! ")
        else:
            print("You've lost! ")
            computer_win += 1
    print(f"Final result is: Computer: {computer_win} User: {user_win}")

if __name__ == "__main__":
    rps_game()
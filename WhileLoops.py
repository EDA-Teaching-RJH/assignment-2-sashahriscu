import random

def main():
# give user instruction
    print("Try to guess the number between 1 and 100")
# number generated
    correct_number = random.randint(1,100)
    guessed_number = None

    while guessed_number != correct_number:
# prompt user to guess number
        guessed_number = int(input("Enter your guess: "))
      
        if guessed_number < correct_number:
            print("Too low")
        elif guessed_number > correct_number:
            print("Too high")
        else:
            print(f"Nice, you guessed the correct number : {correct_number}")
            
main()
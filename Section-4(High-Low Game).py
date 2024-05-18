import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    total_score = 0

    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
          
        computer_number = random.randint(1,100)
        player_number = random.randint(1,100)

        print("Your number is ",  player_number)
        choice = input("Do you think your number is higher or lower than computer's: ")

        if choice == "higher" and player_number > computer_number:
            print("You were right! The computer's number was" , computer_number)
            total_score = total_score +1

        elif choice == "lower" and player_number < computer_number:
            print("Yor were right! The computer's number was" , computer_number)
            total_score = total_score +1

        else:
            print("Aww, that's incorrect. The computer's  number was " , computer_number)
    
        print("Your score is now " , total_score)

    print(" ")


    if total_score == NUM_ROUNDS:
        print("wow!You played perfectly!")

    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()

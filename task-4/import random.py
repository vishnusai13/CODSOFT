import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def main():
    user_score = 0
    computer_score = 0
    play_again = 'yes'
    
    while play_again.lower() in ['yes', 'y']:
        print("\n--- Rock-Paper-Scissors Game ---")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, result)
        
        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1
        
        print(f"\nScores: You - {user_score}, Computer - {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ")
    
    print("\nThanks for playing! Final Scores: You - {}, Computer - {}".format(user_score, computer_score))

if __name__ == "__main__":
    main()

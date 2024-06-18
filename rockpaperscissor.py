import random
print("rock:r\npaper:p\nscissors\n")

while True:
    user_input = input("Enter your choice (r, p, s): ")
    while user_input not in ['r', 'p', 's']:
        user_input = input("Invalid choice. Please enter r, p, or s: ")
    
    computer_choice = random.choice(['r', 'p', 's'])
    
    print("user choice",user_input)
    print("computer_choice",computer_choice)
    
    if user_input == computer_choice:
        result = "It's a tie!"
    elif (user_input == 'r' and computer_choice == 's') or \
         (user_input == 's' and computer_choice == 'p') or \
         (user_input == 'p' and computer_choice == 'r'):
        result = "You win!"
    else:
        result = "You lose!"
    
    print(result)
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != 'yes':
        break

print("Thanks for playing!")

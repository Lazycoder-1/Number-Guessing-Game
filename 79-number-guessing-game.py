import random
def game_play():
    user_lives = 5  # Reset user lives at the start of each game
    while True:
        computer_number = random.randint(1, 10)
        user_guess = int(input('Enter any number between 1 and 10: '))

        if user_guess == computer_number:
            print('Voila, You won!')
            break
        elif user_guess > computer_number:
            print(f'Your guess was higher than the computer. The computer guess was {computer_number}')
            user_lives -= 1
            print(f'You have {user_lives} live(s) remaining')
        elif user_guess < computer_number:
            print(f'Your guess was lower than the computer. The computer guess was {computer_number}')
            user_lives -= 1
            print(f'You have {user_lives} live(s) remaining')

        if user_lives == 0:
            print('Game Over')
            break
def play_again():
    while True:
        res = input("Do you want to play again? [Yes/No]: ").strip().lower()
        if res in ['y', 'yes']:
            return True
        elif res in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

# Main game loop
while True:
    game_play()
    if not play_again():
        print('See you again!')
        break

import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""

def get_difficulty():
    while True:
        inpp = input("Choose a difficulty. Type 'easy', 'medium' or 'hard': ").lower()
        if inpp in ['easy', 'medium', 'hard']:
            return inpp
        print("Invalid input! Please type 'easy', 'medium' or 'hard'.")

def get_guess():
    while True:
        try:
            userguess = int(input("Guess a number between 1 and 100: "))
            if 1 <= userguess <= 100:
                return userguess
            print("Please enter a number between 1 and 100!")
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_game(attempts):
    num = random.randint(1, 100)
    for i in range(attempts, 0, -1):
        print(f"\nYou have {i} attempts remaining.")
        userguess = get_guess()
        if userguess == num:
            print("🎉 You guessed it correctly!")
            return True
        elif abs(userguess - num) <= 5:
            print("🔥 Very close!" + (" Too high!" if userguess > num else " Too low!"))
        elif userguess > num:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    print(f"\n💀 You lost! The number was {num}.")
    return False

def show_score(wins, losses):
    total = wins + losses
    winrate = (wins / total * 100) if total > 0 else 0
    print(f"\n🏆 Score — Wins: {wins} | Losses: {losses} | Win Rate: {winrate:.1f}%")

def main():
    print(logo)
    print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")

    difficulty_attempts = {'easy': 10, 'medium': 7, 'hard': 5}
    wins = 0
    losses = 0

    while True:
        difficulty = get_difficulty()
        attempts = difficulty_attempts[difficulty]
        print(f"\n🎮 {difficulty.capitalize()} mode — You have {attempts} attempts. Good luck!")

        result = play_game(attempts)
        if result:
            wins += 1
        else:
            losses += 1

        show_score(wins, losses)

        again = input("\nPlay again? Type 'yes' or 'no': ").lower()
        if again != 'yes':
            print("\nThanks for playing! 👋")
            break

main()





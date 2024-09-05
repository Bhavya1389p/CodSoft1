import random
def get_user_choice():
  while True:
    choice = input("Choose rock, paper, or scissors: ").lower()
    if choice in ['rock', 'paper', 'scissors']:
      return choice
    else:
      print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
def get_computer_choice():
  choices = ['rock', 'paper', 'scissors']
  return random.choice(choices)
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return 'tie'
  elif (user_choice == 'rock' and computer_choice == 'scissors') or  (user_choice == 'scissors' and computer_choice == 'paper') or  (user_choice == 'paper' and computer_choice == 'rock'):
    return 'win'
  else:
    return 'lose'
def play_game():
  user_choice = get_user_choice()
  computer_choice = get_computer_choice()
  print("You chose:", user_choice)
  print("Computer chose:", computer_choice)
  result = determine_winner(user_choice, computer_choice)
  print("Result:", result)
  return result
def main():
  user_score = 0
  computer_score = 0
  while True:
    result = play_game()
    if result == 'win':
      user_score += 1
    elif result == 'lose':
      computer_score += 1
    print("Your score:", user_score)
    print("Computer score:", computer_score)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
      break
if __name__ == "__main__":
  main()
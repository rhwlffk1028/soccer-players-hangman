# This codes allow user to play a hangman game to guess soccer player's name.
# There are about 80 soccer players and it will be randomly chosen so that user can guess.
# Enjoy the game! :)

# Import python random package
import random
# Import logo art module
import logo_art
# Import nba player list module
import soccer_player_list

# Assigning variables from modules
welcome_msg = logo_art.welcome_msg[0]
lives_img = logo_art.stages
player_list = soccer_player_list.soccer_player_list

# Welcome Message
print(welcome_msg)

# Randomly choose the player from the list and create a blank list with length of number of letters
chosen_player = random.choice(player_list)
blank_list = []
for i in range(len(chosen_player)):
	blank_list.append("_")

# Game parameters: lives and end of game status
lives = 6
end_of_game = False

# While loop runs until game ends (either user wins or loses).
while end_of_game == False:
	# Asks user to guess a letter of the player name
	guess = input("Guess a letter: ").lower()

	# It compares user's choice and each index letter
	# if user's choice matches, then it's replaced
	for i in range(len(blank_list)):
		if guess == chosen_player[i]:
			blank_list[i] = guess
		
	# If user's choice was not correct, then user loses 1 life
	if guess not in chosen_player:
		lives -= 1
		print(lives_img[lives])

	print(f"{' '.join(blank_list)}\n")

	# If _ is not in the list, which means all blank is filles,
	# it means that the user correctly guessed before lives run out.
	if "_" not in blank_list:
		print("You win! Congratulations!")
		end_of_game = True

	# If lives reach 0, which means that user did not guess it right,
	# it will show the correct answer and declare user's loss.
	if lives == 0:
		print(f'The correct answer was {chosen_player}.')
		print("You lost but... good luck next time!")
		end_of_game = True
import random
from hangman_arts import stages
from hangman_word_list import word_list

INITIAL_LIVES = 6

chosen_word = random.choice(word_list)

# show_answer = print(chosen_word)

lives = INITIAL_LIVES
display = []
word_lenght = len(chosen_word)
end_of_game = False

for letter in range(word_lenght):
    display.append("_")

while not end_of_game:

    user_guess = input("Guess a letter: ").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter
    
    
    if user_guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game= True
        print("Congratulations! You won!")
    
    print(stages[lives])
        


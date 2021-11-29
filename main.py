#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')



display = []
word_length = len(chosen_word)
for index in range(word_length):
  display.append('_')

print(display)

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()


  for index in range(word_length):
      letter = chosen_word[index]
      if letter == guess:
        display[index] = letter
  print(display)
  
  if "_" not in display:
    end_of_game = True
    print("You win")
 


  

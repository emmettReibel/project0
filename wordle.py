# TASK A: Define a variable 'word' that holds the correct word for the wordle game
word = "CROWN"

# TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
def makeAGuess(guess):
    # TASK C:Define a variable 'hint' that holds an empty string
  hint = ""
  # TASK D: Build a loop that loops from 0 to the length of word
  for i in range(len(word)):
    # TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
    if guess[i] == word[i]:
      hint += "G"
    # TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
    elif guess[i] in word:
      hint += "Y"
    # TASK G: If the previous two conditions are false, add the symbol "-" to the hint
    else:
      hint += "-"
  # TASK H: Return hint
  return hint

def playGame():
  guesses = 6
  # TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
  while guesses > 0:
    # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable
    # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable
    ehint = makeAGuess(input(f"What are we trying to overthrow, newbie?! you have {str(guesses)} guesses left. ").upper())
    # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
    if ehint == "GGGGG":
      guesses = 0
      print("You've done it! Congratulations.")
      break
    # TASK L: Print hint
    print(ehint)
    guesses -= 1
    # TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 
    if guesses == 0 and ehint != "GGGGG":
      print("You failed our movement. Attempt again.")


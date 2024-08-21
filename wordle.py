# TASK A: Define a variable 'word' that holds the correct word for the wordle game
word = "CROWN"

# TASK B: Define a function 'makeAGuess()' that passes in a users guess as a parameter
def makeAGuess(guess):
  

  # TASK C:Define a variable 'hint' that holds an empty string
  hint = ""

  # TASK D: Build a loop that loops from 0 to the length of word
  for i in range(len(word)):
    if guess[i] == word[i]:
      hint += "G"
    elif guess[i] in word:
      hint += "Y"
    else:
      hint += "-"
  return hint
    # TASK E: Check if the current letter of guess matches the current letter of word. If so add the letter "G" to the hint
    
    # TASK F: If the previous condition is fales, check if the current letter of guess is in word at all. If so add the letter "Y" to the hint
    

    # TASK G: If the previous two conditions are false, add the symbol "-" to the hint
    
  # TASK H: Return hint
guesslimit = 0
# TASK I: Build a loop that loops 6 times (representing the number of guesses a user has)
while guesslimit < 6:
  ehint = makeAGuess(input(f"make a 5 letter guess! you have {str(6-guesslimit)} guesses left. ").upper())
  print(ehint)
  guesslimit += 1
  if guesslimit == 6 and ehint != "GGGGG":
    print("You lose! Try again.")

  # TASK J: Define a variable 'guess'. prompt the user for their 5-letter guess and store it in the variable

  # TASK K: Define a variable 'hint' and set the return of makeAGuess(guess) to that variable

  # TASK L: Print hint

  # TASK M: Check if hint = "GGGGG". If so the user has won. Print a win message and break the loop
  

# TASK N: After the loop has finished, meaning the user has run out of guesses, check if hint != "GGGGG". If so, the user has lost. Print a lose message. 

from player import Player
from item import Item  
from character import Character
from wordle import makeAGuess
from wordle import playGame

print("What an interesting looking ship in the distance, with well dressed individuals surrounding it menacingly...")
player_name = input("What is my name? ")
player = Player(player_name, 100)


decision1 = input ("You ponder whether or not you should approach the ship. Do you want to approach the ship? Y/N: ").upper() 
if decision1 == "Y":
    print("You approach the ship and are greeted by a tall, aristocratic man.")
    character = Character("Samuel", 100)
    decision2 = input("The man says: Hello, odd individual who is suspiciously close to my covert operation! What's your name? (tell him? Y/N:) ")
    if decision2 == "Y":
        character.talk_to_player(self, player, "x")
    
else:
    print("You look away from the ship, and continue on your way to Boston.")

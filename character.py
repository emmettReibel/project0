from item import Item
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.given = False
        self.received = False
        self.inventory = []
        

    def talk_to_player(self, player, player_msg):
        if self.name == "Samuel":
            if self.given == False:
                print(f"\n{self.name} says: Apologies, {player.name}! My name is {self.name}. We need your help to throw this tea overboard!")
                YN = input("\nWill you help the revolutionary? Y/N: ").upper()

                if YN == "Y":
                    print(f"\n{self.name} says: Thank you, {player.name}! Take this crate of tea and toss it to the waves!")
                    self.given = True
                    tea_crate = Item("tea_crate", "crate_of_tea")
                    player.inventory.append(tea_crate)
                    print("Tea crate added to your inventory.")

                else:
                    print(f"\n{self.name} says: You are a coward, {player.name}!")

    def fight_player(self, player):
        if self.name == "Samuel":
            print("\nYou won't tell me? Then prepare to meet your end, mysterious scallywag! \nSamuel draws a sword from his hip sheathe; It's a blade of wonderful craft, and fear rises in throat.")

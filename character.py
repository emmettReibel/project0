
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.received = False
        self.inventory = []
        

    def talk_to_player(self, player_name, player_msg):
        if self.name == "Samuel":
            if self.received == False:
                print(f"Hey {player_name}, my name is {self.name}. We need your help to throw this tea overboard! Will you help us?")
                YN = input("Will you help the revolutionary? Y/N: ").upper()

                if YN == "Y":
                    print(f"{self.name} says: Thank you, {player_name}! Take this crate of tea and throw it overboard!")
                    self.received = True
                    self.inventory.append("tea_crate")

                else:
                    print(f"{self.name} says: You are a coward, {player_name}!")
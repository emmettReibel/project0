class Item:
    def __init__(self, type_of_item, description):
        self.type_of_item = type_of_item
        self.description = description
# create item
        
# give player points for using item
    def use_item(self, player):

        #Checks the player's inventory for specific items and awards points accordingly.
        
        #If the player has a "tea_crate" item in their inventory, and uses it, they are awarded 5 points.
        #If the player has a "strange bottle" item in their inventory, and uses it, they are awarded 10 points.

        if type_of_item == "tea_crate" and tea_crate in player.inventory:
            self.points = 5
        elif type_of_item == "strange bottle" and strange_bottle in player.inventory:
            self.points = 10

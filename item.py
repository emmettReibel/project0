class Item:
    def __init__(self, type_of_item, description):
        self.type_of_item = type_of_item
        self.description = description
# create item
        
# give player points for using item
    def use_item(self, player):
        if type_of_item == "tea_crate" and tea_crate in player.inventory:
            self.points = 5
        elif type_of_item == "strange bottle":
            self.points = 10

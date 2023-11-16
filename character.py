class Character:

    def __init__(self, name, health, width, height):
        self.name = name
        self.health = health
        self.size = (width, height)
        self.sword = False
        self.shield = False
        self.boots = False
        self.inventory = [self.sword, self.shield, self.boots]

    def new_item(self, name):
        if name == "sword" or self.sword:
            self.sword = True
        if name == "shield" or self.shield:
            self.shield = True
        if name == "boots" or self.boots:
            self.boots = True

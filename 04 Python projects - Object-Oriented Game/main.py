class GameObject:
    # optional as initializer can just make them. Here for reference
    name = ""
    appearance = ""
    feel = ""
    smell = ""

    def __init__(self, name, appearance, feel, smell):
        self.name = name
        self.appearance = appearance
        self.feel = feel
        self.smell = smell

    def look(self):
        return f"You look at {self.name}. {self.appearance}\n"

    def touch(self):
        return f"You touch the {self.name}. {self.feel}\n"

    def sniff(self):
        return f"You sniff the {self.name}. {self.smell}\n"
    
game_object = GameObject("Knife", "Pointy", "Cutty cutty", "Smeels like bacon")

print(game_object.sniff())

class Room:
    escape_code = 0
    game_objects = []

    def __init__(self, esc_code, game_obj):
        self.escape_code = esc_code
        # self.code_tries = 0
        self.game_objects = game_obj
    
    # def try_code(self):
    #     code_try = input("What is the code?: \n")
        
    #     if code_try == self.escape_code:
    #         print("You found the right code! You win")
    #         return
    #     else:
    #         self.code_tries += 1
    #         if self.code_tries > 3:
    #             print("More than 3 errors. Unfortunately you lose")
    #             return

    def check_code(self, code):
        return self.escape_code == code
    
    def get_game_object_names(self):
        names = []
        for object in self.game_objects:
            names.append(object.name)
        return names

    

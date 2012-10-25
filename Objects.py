import pygame

MOB_WIDTH = 64
MOB_HEIGHT = 128
class Mob():
    mob_position = 0,0
    mob_type = ""
    location = ""
    image = 'fileDir'
    #animated = False
    
    def __init__(self, mob_type, location, images):
        self.type = type
        self.location = location
        self.image = images
    def set_location(self, new_location):
        self.location = new_location
    def set_position(self, x, y):
        self.mob_position = x, y
    def get_location(self):
        return self.location
    def get_type(self):
        return self.type
    def get_image(self):
        return pygame.image.load(self.image).convert()
    def get_position(self):
        return self.mob_position
    

class Location():
    
    name = ""
    mobs_at_location = []
    def __init__(self, location_name):
        self.name = location_name
        
    
    def remove_mob(self, Mob):
        self.mobs_at_location.remove(Mob)
    def add_mob(self, Mob):
        self.mobs_at_location.append(Mob)
    def add_mobs(self, mobArray):
        self.mobs_at_location.append(mobArray)
    def get_mobs(self):
        return self.mobs_at_location
    def get_number_of_mobs_at_location(self):
        return self.mobs_at_location.__len__()
   
    
        
class Elevator(Location):
    image_path = "lift.jpg"
    Location.name = "elevator"
    current_location = "lobby"
    elevator_position = (0,0)
    
    
    def move(self):
        #Play animation
        if(self.current_location == "lobby"):
            self.current_location = "penthouse"
        else:
            self.current_location = "lobby"
    def set_position(self, position_in):
        self.elevator_position = position_in
    def check_full(self):
        if(len(Location.mobs_at_location) == 2):
            return True
        else:
            return False
    def get_image(self):
        return pygame.image.load(self.image_path).convert()    
    
class Mob():
    MOB_WIDTH = 64
    MOB_HEIGHT = 128
    mob_position = 0,0
    mob_type = ""
    location = ""
    image = 'fileDir'
    animated = False
    
    def __init__(self, mob_type, location, images, animated):
        self.type = type
        self.location = location
        self.image = images
        self.animated = animated
    def set_location(self, new_location):
        self.location = new_location
    def set_position(self, x, y):
        self.mob_position = x, y
    def get_location(self):
        return self.location
    def get_type(self):
        return self.type
    def get_image(self):
        return self.image
    def get_position(self):
        return self.mob_position
    

class Location():
    
    name = ""
    mobs_at_location = []
    image_path = ""
    def __init__(self, location_name, image_directory):
        self.name = location_name
        self.image_path = image_directory
        
    
    def remove_mob(self, Mob):
        self.mobs_at_location.remove(Mob)
    def add_mob(self, Mob):
        self.mobs_at_location.append(Mob)
    def get_mobs(self):
        return self.mobs_at_location
    def get_number_of_mobs_at_location(self):
        return self.mobs_at_location.__len__()
   
    
        
class Elevator(Location):
    Location.name = "elevator"
    full = False
    current_location = "lobby"
    
    
    def move(self):
        #Play animation
        if(self.current_location == "lobby"):
            self.current_location = "penthouse"
        else:
            self.current_location = "lobby"
            
    def check_full(self):
        if(len(Location.mobs_at_location) == 2):
            self.full = True
            return True
        else:
            return False
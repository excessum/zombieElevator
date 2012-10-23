import pygame

import Objects
import sys
        
def main():
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 558
    NUMBER_OF_HUMANS = 3
    NUMBER_OF_ZOMBIES = 3
    humanArray = []
    zombieArray = []
    counter = 0
    print 'hello'
   
    
    elevator = Objects.Elevator('elevator' , "elevator.png")
    #elevator.__init__('elevator' , "elevator.png")
    lobby = Objects.Location('lobby' , "lobby.png")
    #lobby.__init__('lobby' , "lobby.png")
    penthouse = Objects.Location ('penthouse' , "penthouse.png")
    #penthouse.__init__('penthouse' , "penthouse.png")
    current_location = lobby
    running = 1
    
    
    #CHARACTER_WIDTH = 64
    #CHARACTER_HEIGHT = 128
    
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while counter != NUMBER_OF_HUMANS:
        filename = 'Human'.__add__(str(counter+1)).__add__(".gif")
        tempHuman = Objects.Mob('human', 'lobby', filename, False)
        #tempHuman.__init__('human', 'lobby', filename, False)
        tempHuman.set_position(((counter*100)+50), 400)
        humanArray.append(tempHuman)
        counter += 1    
    counter = 0
    while counter != NUMBER_OF_ZOMBIES:
        filename = 'Zombie'.__add__(str(counter+1)).__add__(".gif")
        tempZombie = Objects.Mob('zombie', 'lobby', filename, False)
        tempZombie.set_position((1024-50)-(counter*100), 400)
    
        zombieArray.append(tempZombie)
        counter += 1
    counter = 0
    
    
    
    while running:
        
        for event in pygame.event.get():
            selected_mob = None
            if event.type == pygame.QUIT:
                sys.exit()
            if pygame.mouse.get_pressed() == (True, False, False):
                counter = 0
                mouse_position = pygame.mouse.get_pos()
                selected_mob = None
                while counter < NUMBER_OF_HUMANS:
                    x_tolerance = humanArray[counter].CHARACTER_WIDTH 
                    y_tolerance = humanArray[counter].CHARACTER_HEIGHT
                    x,y = humanArray[counter].get_position
                    location_rect = pygame.Rect(x, y , x+x_tolerance, y+y_tolerance )
                    if location_rect.collidepoint(mouse_position):
                        selected_mob = humanArray[counter]
                while counter < NUMBER_OF_ZOMBIES:
                    x_tolerance = zombieArray[counter].CHARACTER_WIDTH 
                    y_tolerance = zombieArray[counter].CHARACTER_HEIGHT
                    x,y = zombieArray[counter].get_position
                    location_rect = pygame.Rect(x, y , x+x_tolerance, y+y_tolerance )
                    if location_rect.collidepoint(mouse_position):
                        selected_mob = humanArray[counter]
            
                
                
        print ''+current_location.image_path
        background = pygame.image.load(current_location.image_path).convert()
        screen.blit(background, (0, 0))
        print 'current location is ' +current_location.name + ' and human location is ' +humanArray[0].location
        counter = 0
        while counter < NUMBER_OF_HUMANS:
            tempImage = pygame.image.load(humanArray[counter].image).convert()
            screen.blit(tempImage, (humanArray[counter].get_position()))           
            counter += 1
        while counter < NUMBER_OF_ZOMBIES:
            tempImage = pygame.image.load(zombieArray[counter].image).convert()
            screen.blit(tempImage, (zombieArray[counter].get_position))           
            counter += 1
    
        
        pygame.display.update()
        
        #Wait until mouse clicked on Mob object
        #Update the draw as the mouse is dragged to the elevator
        #move mobs from current location to elevator 
        #Once elevator is full close doors
        #Check for an upwards drag
        #Move mobs from one place to another
        #Check previous location for either loss or win   

def move_mob(mob, from_location, to_location):
    from_location.remove_mob(mob)
    to_location.add_mob(mob)
    


if __name__ == '__main__':
    main()
    
    
                
        
    
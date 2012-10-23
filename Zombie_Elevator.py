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
    zombieImageArray = []
    humanImageArray = []
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
        tempImage = pygame.image.load(filename)
        humanImageArray.append(tempImage)
        humanArray.append(tempHuman)
        counter += 1    
    counter = 0
    while counter != NUMBER_OF_ZOMBIES:
        filename = 'Zombie'.__add__(str(counter+1)).__add__(".gif")
        tempZombie = Objects.Mob('zombie', 'lobby', filename, False)
        tempImage = pygame.image.load(filename)
        zombieImageArray.append(tempImage)
        zombieArray.append(tempZombie)
        counter += 1
    counter = 0
    
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        print ''+current_location.image_path
        background = pygame.image.load(current_location.image_path).convert()
        screen.blit(background, (0, 0))
        print 'current location is ' +current_location.name + ' and human location is ' +humanArray[0].location
        if humanArray[0].location == current_location.name :
            screen.blit(humanImageArray[0], (50, 400))
        if humanArray[1].location == current_location.name :
            screen.blit(humanImageArray[1], (150, 400))
        if humanArray[2].location == current_location.name :
            screen.blit(humanImageArray[2], (250, 400))
        
        if zombieArray[0].location == current_location.name :
            screen.blit(zombieImageArray[0], (725, 400))
        if zombieArray[1].location == current_location.name :
            screen.blit(zombieImageArray[1], (825, 400))
        if zombieArray[2].location == current_location.name :
            screen.blit(zombieImageArray[2], (925, 400))
        
        pygame.display.update()
        
        #Wait until mouse clicked on Mob object
        #Update the draw as the mouse is dragged to the elevator
        #move mobs from current location to elevator 
        #Once elevator is full close doors
        #Check for an upwards drag
        #Move mobs from one place to another
        #Check previous location for either loss or win   

   


if __name__ == '__main__':
    main()
    
    
                
        
    
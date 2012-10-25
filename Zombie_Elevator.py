import pygame

import Objects
import sys

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768   
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
human1 = Objects.Mob('human', 'lobby', 'Human1.png')
human2 = Objects.Mob('human', 'lobby', 'Human2.png')
human3 = Objects.Mob('human', 'lobby', 'Human3.png')
zombie1 = Objects.Mob('zombie', 'lobby', 'Zombie1.png')
zombie2 = Objects.Mob('zombie', 'lobby', 'Zombie2.png')
zombie3 = Objects.Mob('zombie', 'lobby', 'Zombie3.png')
elevator = Objects.Elevator('elevator')
LOBBY_ELEVATOR_POSITION = (10,550) #PLACEHOLDER FOR POSITION OF ELEVATOR AT LOBBY
PENTHOUSE_ELEVATOR_POSITION = (5,0) #PLACEHODLER FOR POSITION OF ELEVATOR AT LOBBY
elevator.set_position(LOBBY_ELEVATOR_POSITION)
def main():
    lobby = Objects.Location('lobby')
    penthouse = Objects.Location ('penthouse')
    running = 1
    
    
    
    lobby.add_mob(human1)
    lobby.add_mob(human2)
    lobby.add_mob(human3)
    lobby.add_mob(zombie1)
    lobby.add_mob(zombie2)
    lobby.add_mob(zombie3)
    human1.set_position(50, 400)
    human2.set_position(150, 400)
    human3.set_position(250,400)
    zombie1.set_position(975, 400)
    zombie2.set_position(875, 400)
    zombie3.set_position(775, 400)
    selected_mob = human1
    
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_mob = human1
                    print 'human 1 selected'
                elif event.key == pygame.K_2:
                    selected_mob = human2
                    print 'human 2 selected'
                elif event.key == pygame.K_3:
                    selected_mob = human3
                    print 'human 3 selected'
                elif event.key == pygame.K_4:
                    selected_mob = zombie3
                    print 'zombie 1 selected'
                elif event.key == pygame.K_5:
                    selected_mob = zombie2
                    print 'zombie 2 selected'
                elif event.key == pygame.K_6:
                    selected_mob = zombie1
                    print 'zombie 3 selected'
                if event.key == pygame.K_LEFT:
                    print 'left key pressed'
                    if selected_mob.get_location() != "elevator":    
                        if selected_mob.get_location() == "lobby":
                            if elevator.current_location == "lobby":
                                if elevator.check_full() == False:
                                    lobby.remove_mob(selected_mob)
                                    elevator.add_mob(selected_mob)
                                    x, y = LOBBY_ELEVATOR_POSITION
                                    selected_mob.set_position(x,y) #PLACE HOLDER FOR WHERE GROUND ELEVATOR IS LOCATE
                            else:
                                if elevator.current_location == "penthouse":
                                    if elevator.check_full():
                                        penthouse.remove_mob(selected_mob)
                                        elevator.add_mob(selected_mob)
                                        selected_mob.set_pos(PENTHOUSE_ELEVATOR_POSITION) # PLACE HOLDER FOR PENTHOUSE ELEVATOR
                if event.key == pygame.K_RIGHT:
                    print 'right key pressed'
                    if selected_mob.get_location() == elevator:
                        if elevator.current_location == "lobby":
                            selected_mob.set_position(0,0) # PLACE THE MOB IN THE LOBBY
                            elevator.remove_mob(selected_mob)
                            lobby.add_mob(selected_mob)
                        else:
                            selected_mob.set_position(0,0) # PLACE THE MOB IN THE PENTHOUSE
                            elevator.remove_mob(selected_mob)
                            lobby.add_mob(selected_mob)
                        if elevator.mobs_at_location.__len__() == 0:
                            if penthouse.get_number_of_mobs_at_location() == 6:
                                victory()
                            else:
                                loop_counter = 0
                                z_counter = 0
                                h_counter = 0
                                #################################################
                                ####    Loop through penthouse to check for   ###
                                ####        victory or defeat conditions      ###
                                #################################################
                                while loop_counter < penthouse.get_number_of_mobs_at_location():                     
                                    if penthouse.mobs_at_location[loop_counter].get_type == 'zombie':
                                        z_counter += 1
                                    else:
                                        h_counter += 1
                                    loop_counter +=1
                                                                       
                                if z_counter > h_counter:
                                    game_over()
                                #################################################
                                ###########Reset all the counters################
                                ################################################# 
                                loop_counter = 0
                                z_counter = 0
                                h_counter = 0
                                
                                #################################################
                                ####       Loop through lobby to check for    ###
                                ####        victory or defeat conditions      ###
                                #################################################
                            
                                while loop_counter < lobby.get_number_of_mobs_at_location():
                                    if penthouse.mobs_at_location[loop_counter].get_type == 'zombie':
                                        z_counter += 1
                                    else:
                                        h_counter += 1
                                    loop_counter +=1
                                                                       
                                if z_counter > h_counter:
                                    game_over()
                                
                if event.key == pygame.K_UP:
                    if elevator.current_location == 'lobby':
                        if elevator.get_number_of_mobs_at_location() == 0:
                            pass
                        else:
                            move_elevator('up')
                            elevator.move()
                if event.key == pygame.K_DOWN:
                    if elevator.current_location == 'penthouse':
                        if elevator.get_number_of_mobs_at_location() == 0:
                            pass
                        else:
                            move_elevator('down')
                            elevator.move()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print pygame.mouse.get_pos()
                
        
        background = pygame.image.load('background.jpg').convert()
        screen.blit(background, (0, 0))
        
        
        
    
        repaint()
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
    
def victory():
    #Do victory procedure
    print 'victory!'

def game_over():
    #Do game over procedure
    print 'game over!'

def move_elevator(direction):
    e_starting_pos_x, e_starting_pos_y = (LOBBY_ELEVATOR_POSITION)
    e_end_pos_x, e_end_pos_y = (PENTHOUSE_ELEVATOR_POSITION)
    m1_starting_pos_x, m1_starting_pos_y = (0,0)    
    m1_end_pos_y = m1_starting_pos_y - (e_starting_pos_y - e_end_pos_y)
    m2_starting_pos_x, m2_starting_pos_y = (0,0)
    m2_end_pos_y = m2_starting_pos_y - (e_starting_pos_y - e_end_pos_y)
    count = 0
    while count < elevator.mobs_at_location.__len__():
        m1_starting_pos_x, m1_starting_pos_y = elevator.mobs_at_location[count].get_position()
        m2_starting_pos_x, m2_starting_pos_y = elevator.mobs_at_location[count].get_position()
    count = 0
    if direction == 'up':
        while e_starting_pos_y < e_end_pos_y:
            if (e_starting_pos_y + 5) < e_end_pos_y:
                elevator.mobs_at_location[0].set_pos(m1_starting_pos_x, m1_starting_pos_y-m1_end_pos_y)
                elevator.mobs_at_location[1].set_pos(m2_starting_pos_x, m2_starting_pos_y-m2_end_pos_y)
                elevator.set_position(PENTHOUSE_ELEVATOR_POSITION)
            elevator.mobs_at_location[1].set_pos(m2_starting_pos_x, m2_starting_pos_y-(count*5-5))
            elevator.mobs_at_location[0].set_pos(m1_starting_pos_x, m1_starting_pos_y-(count*5-5))
            elevator.set_position(e_starting_pos_x, e_starting_pos_y-(count*5-5))
            repaint()
            pygame.display.update()
    if direction == 'down':
        while e_starting_pos_y > e_end_pos_y:
            if (e_starting_pos_y + 5) > e_end_pos_y:
                elevator.mobs_at_location[0].set_pos(m1_starting_pos_x, m1_starting_pos_y+m1_end_pos_y)
                elevator.mobs_at_location[1].set_pos(m2_starting_pos_x, m2_starting_pos_y+m1_end_pos_y)
                elevator.set_position(LOBBY_ELEVATOR_POSITION)
            elevator.mobs_at_location[1].set_pos(m2_starting_pos_x, m2_starting_pos_y-(count*5-5))
            elevator.mobs_at_location[0].set_pos(m1_starting_pos_x, m1_starting_pos_y-(count*5-5))
            elevator.set_position(e_starting_pos_x, m1_starting_pos_y-(count*5-5))
            repaint()
            pygame.display.update()     
        elevator.move()
def repaint():
    screen.blit(human1.get_image(), human1.get_position())
    screen.blit(human2.get_image(), human2.get_position())
    screen.blit(human3.get_image(), human3.get_position())
    screen.blit(zombie1.get_image(), zombie1.get_position())
    screen.blit(zombie2.get_image(), zombie2.get_position())
    screen.blit(zombie3.get_image(), zombie3.get_position())
    screen.blit(elevator.get_image(), elevator.elevator_position)
if __name__ == '__main__':
    main()
    
    
                
        
    
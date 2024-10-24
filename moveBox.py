"""Marianne Adams
CS120 Basic Animation
Move Box"""
#import
import pygame
def main():
    pygame.init()
    
    #display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move a Box")
    
    #Entities
    #Want a pink background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,119,130))
    
    #make a green 25x25 box
    box = pygame.Surface((25, 25))
    box = box.convert()
    box.fill((62, 180, 137))
    
    #set up box variables
    box_x = 0
    box_y = 200
    
    #Action
    #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
    #Loop
    while keepGoing:
        #time
        clock.tick(30)
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #modify box value
        box_x += 5
        #check boundaries
        if box_x > screen.get_width():
            box_x = 0
        #refresh
        screen.blit(background,(0,0))
        screen.blit(box,(box_x, box_y))
        pygame.display.flip()
    pygame.quit()
     
if __name__=="__main__":
    main()
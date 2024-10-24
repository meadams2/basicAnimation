"""Marianne Adams
CS120
Wednesday's Adventure"""
import pygame
import random

def  main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Wednesday's Adventure! Press <space> for new direction, <m> to change bound mode")
    
    #Entities
    #Create background
#     background = pygame.Surface(screen.get_size())
    background = pygame.image.load("BackgroundImage.png")
    background.convert()
    background = pygame.transform.scale(background, (640, 480))
    
    #Create moving object
    wednesday = pygame.image.load("Wednesday.png")
    wednesday.convert_alpha()
    wednesday = pygame.transform.scale(wednesday, (100, 100))
    wednesday_x = 320
    wednesday_y = 240
    
    #Action
    #Assign variables
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    clock = pygame.time.Clock()
    keepGoing = True
    mode = "bounce"
    
    #Set up loop
    while keepGoing:
        #Time
        clock.tick(30)
        #Event-handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dx = random.randint(-10, 10)
                    dy = random.randint(-10, 10)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    if mode == "bounce":
                        mode = "wrap"
                    else:
                        mode = "bounce"
        wednesday_x += dx
        wednesday_y += dy
        
        if mode == "bounce":
            #Bounce - using the size of image
            w_rect = wednesday.get_rect()
            w_rect.left = wednesday_x
            w_rect.top = wednesday_y
            
            if w_rect.right > screen.get_width():
                dx *= -1
            if w_rect.left < 0:
                dx *= -1
            if w_rect.top < 0:
                dy *= -1
            if w_rect.bottom > screen.get_height():
                dy *= -1
        else:
            #wrap
            if wednesday_x > screen.get_width():
                wednesday_x = 0
            if wednesday_x < 0:
                wednesday_x = screen.get_width()
            
            if wednesday_y > screen.get_height():
                wednesday_y = 0
            if wednesday_y < 0:
                wednesday_y = screen.get_height()
        
        #Refresh
        screen.blit(background, (0,0))
        screen.blit(wednesday, (wednesday_x, wednesday_y))
        
        pygame.display.flip()
        
    pygame.quit()

if __name__=="__main__":
    main()
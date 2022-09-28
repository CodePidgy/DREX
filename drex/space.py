import sys
import pygame

pygame.init()

class Space:

    def displayWindow():

        window = pygame.display.set_mode([500,500])

        ball = pygame.image.load("E:\\gitClone\\DREX\\ball.png").convert()
        
        ball = pygame.transform.scale(ball, (50,50))    

        window.blit(ball, (1,1))
        window.blit(ball, (50,50))
        window.blit(ball, (100,100))

        pygame.display.flip()

        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
    displayWindow()









                
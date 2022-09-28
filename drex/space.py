from contextlib import redirect_stderr
import sys
import pygame

pygame.init()


class Space:
    def displayWindow():

        window = pygame.display.set_mode([500, 500])

        pygame.draw.circle(window, [250, 250, 250, 0], (25, 25), 25)

        pygame.draw.circle(window, [250, 250, 250, 0], (75, 75), 25)

        pygame.draw.circle(window, [250, 250, 250, 0], (150, 150), 25)

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

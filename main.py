# system imports --------------------------------------------------------------------- #
import sys

# third-party imports ---------------------------------------------------------------- #
import pygame

# local imports ---------------------------------------------------------------------- #
from drex import Vector
from drex.shape import Line

# constants -------------------------------------------------------------------------- #
DISPLAY_SIZE = [100, 100]
WINDOW_SIZE = [200, 200]
FPS = 60

# set up pygame ---------------------------------------------------------------------- #
pygame.init()
pygame.display.set_caption("DREX")

clock = pygame.time.Clock()
display = pygame.Surface(DISPLAY_SIZE)
window = pygame.display.set_mode(WINDOW_SIZE)

# set up drex ------------------------------------------------------------------------ #

# general variables ------------------------------------------------------------------ #
font = pygame.font.SysFont("Arial", 15)

# misc ------------------------------------------------------------------------------- #

# loop ------------------------------------------------------------------------------- #
while True:
    # background --------------------------------------------------------------------- #
    display.fill([0, 0, 0])

    # logic -------------------------------------------------------------------------- #
    fps = int(clock.get_fps())
    fps_text = font.render(f"FPS: {fps}", False, [255, 255, 255])

    # render ------------------------------------------------------------------------- #

    # buttons ------------------------------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # update ------------------------------------------------------------------------- #
    window.blit(pygame.transform.scale(display, window.get_size()), [0, 0])
    window.blit(fps_text, [0, 0])

    pygame.display.update()

    clock.tick(FPS)

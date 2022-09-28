# system imports --------------------------------------------------------------------- #
import sys

# third-party imports ---------------------------------------------------------------- #
import pygame

# space class ------------------------------------------------------------------------ #
class Space:
    # initialisation ----------------------------------------------------------------- #
    def __init__(self, window_size: list) -> None:
        if type(window_size) != list:
            raise TypeError(
                f"'window_size' must be of type 'list', not {type(window_size)}"
            )

        self.__window_size = window_size

        self.display_size = window_size
        self.fps = 60
        self.background = [0, 0, 0]

        self.__title = "DREX"
        self.__show_fps = False

        pygame.init()

        self.__window = pygame.display.set_mode(self.__window_size)
        self.__display = pygame.Surface(self.__display_size)
        self.__clock = pygame.time.Clock()

    # properties --------------------------------------------------------------------- #
    @property
    def display_size(self) -> list:
        return self.__display_size

    @display_size.setter
    def display_size(self, display_size: list) -> None:
        if type(display_size) != list:
            raise TypeError(
                f"'display_size' must be of type 'list', not {type(display_size)}"
            )

        if len(display_size) != 2:
            raise ValueError("'display_size' must have a length of 2")

        self.__display_size = display_size

    @property
    def fps(self) -> int:
        return self.__fps

    @fps.setter
    def fps(self, fps: int) -> None:
        if type(fps) != int:
            raise TypeError(f"'fps' must be of type 'int', not {type(fps)}")

        self.__fps = fps

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        if type(title) != str:
            raise TypeError(f"'title' must be of type 'str', not {type(title)}")

        self.__title = title

        pygame.display.set_caption(self.__title)

    # private methods ---------------------------------------------------------------- #
    def __events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def __update(self) -> None:
        self.__display.fill([0, 0, 0])

        self.__window.blit(
            pygame.transform.scale(self.__display, self.__window.get_size()), [0, 0]
        )

        if self.__show_fps:
            self.__window.blit(
                pygame.font.SysFont("Arial", 15).render(
                    f"FPS: {int(self.__clock.get_fps())}", False, [255, 255, 255]
                ),
                [0, 0],
            )

        pygame.display.update()

        self.__clock.tick(self.__fps)

    # public methods ----------------------------------------------------------------- #
    def show_fps(self, show: bool) -> None:
        if type(show) != bool:
            raise TypeError(f"'show' must be of type 'bool', not {type(show)}")

        self.__show_fps = show

    def step(self) -> None:
        self.__events()
        self.__update()

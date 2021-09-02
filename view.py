import pygame
import constants as consts

class View:
    def __init__(self,model):
        self.screen= pygame.display.set_mode((consts.WIDTH,consts.HEIGHT))
        self.clock = pygame.time.Clock()

        self.model=model

    def updateView(self):
        self.screen.fill(consts.GREY)
        pygame.display.update()
        self.clock.tick(consts.FPS)


import pygame, sys
from config import *
from fase import *


class Jogo:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Lights out')
        self.clock = pygame.time.Clock()

        self.fase = Fase()
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.fase.run()
            pygame.display.update()
            self.clock.tick(FPS)
    

if __name__ == '__main__':
    jogo = Jogo()
    jogo.run()
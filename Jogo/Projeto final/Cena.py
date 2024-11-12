import pygame
from config import *


# class Parede(pygame.sprite.Sprite):
#     def __init__(self,pos,groups):
#         super().__init__(groups)
#         self.image = pygame.image.load('imagens/arbusto.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft = pos)
#         self.hitbox = self.rect.inflate(0,-10)

class Objetos(pygame.sprite.Sprite):
    def __init__(self,pos,groups,im,x,y):
        super().__init__(groups)
        self.image = pygame.image.load(im).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(x,y)

class Interface:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

        self.barra_vida = pygame.Rect(10,10,LARGURA_BARRA_VIDA, ALTURA_BARRA)
        
    def barra(self, atual, max, bg_rect, cor):
        pygame.draw.rect(self.display_surf, BG_COR, bg_rect)

        status_vida = atual/max
        barra_tam = bg_rect.width * status_vida
        barra_rect = bg_rect.copy()
        barra_rect.width = barra_tam

        pygame.draw.rect(self.display_surf,cor, barra_rect)
        pygame.draw.rect(self.display_surf, BORDA_COR, bg_rect,2)
        

    def display(self, player):
        self.barra(player.vida, player.estado['vida'], self.barra_vida, COR_VIDA)
        
        






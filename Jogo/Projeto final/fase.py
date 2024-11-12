from pickle import TRUE
import pygame
from config import *
from Personagens import *
from Cena import *
from banco import *

class Fase:
    def __init__(self):     
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSort()
        self.obstacle_sprites = pygame.sprite.Group()
        self.ataca_sprites = pygame.sprite.Group()
        self.atacado_sprites = pygame.sprite.Group()
        self.mapa()

        self.interface = Interface()
        
        self.score = 0
        self.high_score = 0
        self.lanterna_score = False

    def mapa(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index *TILESIZE
                y = row_index *TILESIZE
                if col == 'p':
                    self.persona = Personagem((x,y),[self.visible_sprites],self.obstacle_sprites, self.cria_ataque, self.deleta_ataque)
                if col == 'I':
                    Monstro((x,y),[self.visible_sprites, self.atacado_sprites], self.obstacle_sprites, self.player_dano)
                    
                # if col == 'X':
                #     Parede((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'D':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/casa_dir.png',0,-40)
                if col == 'L':
                    self.lanterna = Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/lanterna.png',-16,-16)
                if col == 'C':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/cone.png',0,-40)
                if col == '0':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/blank.png',0,-40)
                if col == 'X':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/blank2.png',0,0)
                if col == 'E':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/casa_esq.png',-20,-20)
                if col == 'K':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/konbini.png',0,-20)
                if col == 'M':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/muro.png',0,-20)
                if col == 'A':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/arbusto.png',-10,-20)
                if col == 'B':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/balanco.png',0,-20)
                if col == 'O':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/bola.png',-10,-5)
                if col == 'R':
                    Objetos((x,y), [self.visible_sprites, self.obstacle_sprites],'imagens/brinquedo.png',-5,-20)

        self.fundo = pygame.image.load("imagens/fundo.png").convert()
        self.fundo_rect = self.fundo.get_rect(topleft = (0,0))
        
    def cria_ataque(self):
        self.Ataque = Ataque(self.persona,[self.visible_sprites, self.ataca_sprites])

    # def cria_ataque(self, forca, custo):
    #     print(forca)
    #     print(custo)

    def deleta_ataque(self):
        if self.Ataque:
            self.Ataque.kill()
        self.Ataque = None

    def player_dano(self, dano):
        if self.persona.vulneravel:
            self.persona.vida -= dano
            self.persona.vulneravel = False
            self.persona.dano_time = pygame.time.get_ticks()

    def player_ataque(self):

        if self.ataca_sprites:
            for ataca_sprite in self.ataca_sprites:
                colide_sprite = pygame.sprite.spritecollide(ataca_sprite,self.atacado_sprites,False)
                if colide_sprite:
                    for target_sprite in colide_sprite:
                        if target_sprite.tipo_sprite == 'monstro':
                            target_sprite.get_damage(self.persona,ataca_sprite.tipo_sprite)
                            self.score +=1

    def update_highscore(self,score, high_score):
        if score > high_score:
            high_score = score
        return high_score

    def score_display(self, game_state):
        self.fonte = pygame.font.Font('pixelart.ttf', 18)

        if game_state == 'jogando':
            score_text_surf = self.fonte.render(f'Score: {int(self.score)}', True, (255,255,255))
            score_text_rect = score_text_surf.get_rect(center = (80,650))
            self.display_surface.blit(score_text_surf, score_text_rect)

        if game_state == 'game_over':
            score_text_surf = self.fonte.render(f'Score: {int(self.score)}', True, (255,255,255))
            score_text_rect = score_text_surf.get_rect(center = (80,650))
            self.display_surface.blit(score_text_surf, score_text_rect)

        highscore_text_surf = self.fonte.render(f'Highscore: {int(self.high_score)}', True, (255,255,255))
        highscore_text_rect = highscore_text_surf.get_rect(center = (750,650))
        self.display_surface.blit(highscore_text_surf, highscore_text_rect)



    def Pegar(self):

        for L in WORLD_MAP:
            if pygame.key.get_pressed()[pygame.K_f] and self.lanterna.rect.colliderect(self.persona.hitbox):
                self.lanterna.kill()
                self.score =+ 1


    def run(self):
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()
        self.Pegar()
        self.visible_sprites.monstro_up(self.persona)
        self.player_ataque()
        self.interface.display(self.persona)
        self.score_display('jogando')
        self.update_highscore(self.score,self.high_score)
        teste



class Ataque(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        self.tipo_sprite = 'ataque'
        dir = player.status.split('_')[0]

        self.image = pygame.image.load('imagens/lanterna_blank.png').convert_alpha()

        if dir == 'direita':
            self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(-12,10))
        elif dir == 'esquerda':
            self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(10,10))
        elif dir == 'baixo':
            self.rect = self.image.get_rect(midtop = player.rect.midbottom)
        else:
            self.rect = self.image.get_rect(midbottom = player.rect.midtop)
       


class YSort(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.fundo = pygame.image.load('imagens/fundo.png').convert()
        self.fundo_rect = self.fundo.get_rect(topleft = (0,0))

    def custom_draw(self):

        self.display_surface.blit(self.fundo,self.fundo_rect)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)
        
    def monstro_up(self, player):
        monstro_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'tipo_sprite') and sprite.tipo_sprite == 'monstro']
        for monstro in monstro_sprites:
            monstro.monstro_up(player)





    
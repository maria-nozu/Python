import pygame
from config import *
from fase import *
from math import sin

class Personagem(pygame.sprite.Sprite):


    def __init__(self, pos, groups, obstacle, cria_ataque, deleta_ataque):
        super().__init__(groups)
        self.image = pygame.image.load('imagens/menino/menino_lado_d1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-5)

        self.frames()
        self.frame = 0
        self.frame_vel = 0.15
        self.status = 'baixo'

        self.dir = pygame.math.Vector2()
        self.Ataque = False
        self.ataq = False
        self.ataque_c = 400
        self.ataque_t = None


        self.cria_ataque = cria_ataque
        self.deleta_ataque = deleta_ataque
        self.obstacle = obstacle
       

        self.estado = {'vida': 200, 'ataque':30, 'velocidade': 2, 'energia':1}
        self.vida = self.estado['vida']
        self.vel = self.estado['velocidade']
        self.energia = self.estado['energia']

        self.vulneravel = True
        self.hurt_time = 0
        self.invi_time = 500


    def frames(self):
        self.direita = [pygame.image.load('imagens/menino/menino_lado_d1.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_lado_d2.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_lado_d3.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_lado_d4.png').convert_alpha()]

        self.esquerda = [pygame.image.load('imagens/menino/menino_lado_e1.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_lado_e2.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_lado_e3.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_lado_e4.png').convert_alpha()]

        self.baixo = [pygame.image.load('imagens/menino/menino_f1.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_f2.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_f3.png').convert_alpha(),
                        pygame.image.load('imagens/menino/menino_f4.png').convert_alpha()]

        self.cima = [pygame.image.load('imagens/menino/menino_t1.png').convert_alpha(),
                    pygame.image.load('imagens/menino/menino_t2.png').convert_alpha(),
                    pygame.image.load('imagens/menino/menino_t3.png').convert_alpha(),
                    pygame.image.load('imagens/menino/menino_t4.png').convert_alpha()]
        
        self.parado_baixo = [pygame.image.load('imagens/menino/menino_f1.png').convert_alpha()]

        self.parado_cima = [pygame.image.load('imagens/menino/menino_t1.png').convert_alpha()]

        self.parado_direita = [pygame.image.load('imagens/menino/menino_lado_d1.png').convert_alpha()]

        self.parado_esquerda = [pygame.image.load('imagens/menino/menino_lado_e1.png').convert_alpha()]
        
        self.ataque_d = [pygame.image.load('imagens/menino/menino_ataq_d2.png').convert_alpha()]
        
        self.ataque_e = [pygame.image.load('imagens/menino/menino_ataq_e2.png').convert_alpha()]

        self.ataque_f = [pygame.image.load('imagens/menino/menino_ataq_f1.png').convert_alpha()]

        self.ataque_t = [pygame.image.load('imagens/menino/menino_ataq_t1.png').convert_alpha()]

        self.animacoes = {'cima':self.cima, 'baixo':self.baixo, 'esquerda':self.esquerda, 
                        'direita':self.direita, 'cima_parado':self.parado_cima,'baixo_parado':self.parado_baixo,
                        'esquerda_parado':self.parado_esquerda,'direita_parado':self.parado_direita,
                        'direita_ataque':self.ataque_d, 'esquerda_ataque':self.ataque_e, 'cima_ataque':self.ataque_t,
                        'baixo_ataque': self.ataque_f}


    def input(self):
        if not self.ataq:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.dir.y = -1
                self.status = 'cima'
            elif keys[pygame.K_DOWN]:
                self.dir.y = 1
                self.status = 'baixo'
            else:
                self.dir.y = 0

            if keys[pygame.K_RIGHT]:
                self.dir.x = 1
                self.status = 'direita'
            elif keys[pygame.K_LEFT]:
                self.dir.x = -1
                self.status = 'esquerda'
            else:
                self.dir.x = 0


            if keys[pygame.K_SPACE]:
                self.ataq = True
                self.ataque_t = pygame.time.get_ticks()
                self.cria_ataque()

                
    def get_status(self):

        if self.dir.x == 0 and self.dir.y == 0:
            if not 'parado' in self.status and not 'ataque' in self.status:
                self.status = self.status + '_parado'

        if self.ataq:
            
            self.dir.x = 0
            self.dir.y = 0
            if not 'ataque' in self.status:
                if 'parado' in self.status:
                    self.status = self.status.replace('_parado','_ataque')
                else:
                    self.status = self.status + '_ataque'
        else:
            if 'ataque' in self.status:
                self.status = self.status.replace('_ataque','')

    def move(self,vel):
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()

        self.hitbox.x += self.dir.x * vel
        self.colide('x')
        self.hitbox.y += self.dir.y * vel
        self.colide('y')
        self.rect.center = self.hitbox.center

        if self.dir.x > 896: self.dir.x = 0

    def colide(self,dir):
        if dir == 'x':
            for sprite in self.obstacle:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.dir.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.dir.x <0:
                        self.hitbox.left = sprite.hitbox.right

        if dir == 'y':
            for sprite in self.obstacle:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.dir.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.dir.y <0:
                        self.hitbox.top = sprite.hitbox.bottom

    def cria_dano(self):
        dano = self.estado['ataque']
        return dano

    def animacao(self):
        anima = self.animacoes[self.status]
        self.frame += self.frame_vel

        if self.frame >= len(anima):
            self.frame = 0
        self.image = anima[int(self.frame)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def checa_morte(self):
        if self.vida <= 0:
            self.kill()
        
    def pisca(self):
        value = sin(pygame.time.get_ticks())
        if value >=0:
            return 255
        else:
            return 0
    def cooldown(self):
        tempo = pygame.time.get_ticks()

        if self.ataq:
            if tempo - self.ataque_t >= self.ataque_c:
                self.ataq = False
                self.deleta_ataque()

        if not self.vulneravel:
            if tempo - self.hurt_time >= self.invi_time:
                self.vulneravel = True

    def update(self):
        self.input()
        self.cooldown()
        self.get_status()
        self.animacao()
        self.move(self.vel)
        self.checa_morte()


class Monstro(pygame.sprite.Sprite):

    def __init__(self, pos, groups,obstacle, player_dano):
        super().__init__(groups)
        self.tipo_sprite = 'monstro'
        self.image = pygame.image.load('imagens/zeca/zeca_f1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle = obstacle
        self.monstro = {'vida': 300, 'dano':10,'velocidade':1, 'raio_ataque':20, 'raio_visao':360}

        self.frames()
        self.status = 'parado'
        self.atual = 0.15
        self.dir = pygame.math.Vector2()
        self.frame = 0

        self.vel = self.monstro['velocidade']
        self.vida = self.monstro['vida']
        self.dano = self.monstro['dano']
        self.raio_ataque = self.monstro['raio_ataque']
        self.raio_visao = self.monstro['raio_visao']

        self.ataca = True
        self.ataca_time = None
        self.ataca_cooldown = 400

        self.player_dano = player_dano

        self.vulneravel = True
        self.hit_time = None
        self.invi_time = 300

    def frames(self):

        self.baixo = [pygame.image.load('imagens/zeca/zeca_f1.png').convert_alpha(),
                        pygame.image.load('imagens/zeca/zeca_f2.png').convert_alpha(),]
        
        self.parado_y = [pygame.image.load('imagens/zeca/zeca_f1.png').convert_alpha()]
        
        self.ataque_e = [pygame.image.load('imagens/zeca/zeca_ataq_e1.png').convert_alpha(),
                        pygame.image.load('imagens/zeca/zeca_ataq_e2.png').convert_alpha(),
                        pygame.image.load('imagens/zeca/zeca_ataq_e3.png').convert_alpha()
                        ]

        self.animacoes = {'move':self.baixo,'ataque':self.ataque_e, 'parado':self.parado_y}

    def animacao(self):
        self.anima = self.animacoes[self.status]
        self.frame += self.atual
        if self.frame >= len(self.anima):
            if self.status == 'ataque':
                self.ataca = False
            self.frame = 0

        self.image = self.anima[int(self.frame)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulneravel:
            alpha = self.pisca()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def pisca(self):
        value = sin(pygame.time.get_ticks())
        if value >=0:
            return 255
        else:
            return 0

    def move(self,vel):
        if self.dir.magnitude() != 0:
            self.dir = self.dir.normalize()

        self.hitbox.x += self.dir.x * vel
        self.colide('x')
        self.hitbox.y += self.dir.y * vel
        self.colide('y')
        self.rect.center = self.hitbox.center

    def colide(self,dir):
        if dir == 'x':
            for sprite in self.obstacle:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.dir.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.dir.x <0:
                        self.hitbox.left = sprite.hitbox.right

        if dir == 'y':
            for sprite in self.obstacle:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.dir.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.dir.y <0:
                        self.hitbox.top = sprite.hitbox.bottom

    def player_distancia(self,player):
        monstro_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distancia = (player_vec - monstro_vec).magnitude()

        if distancia > 0:
            dir = (player_vec - monstro_vec).normalize()
        else:
            dir = pygame.math.Vector2()

        return (distancia,dir)

    def get_status(self,player):
        distancia = self.player_distancia(player)[0]

        if distancia <= self.raio_ataque and self.ataca:
            if self.status != 'ataque':
                self.frame = 0
            self.status = 'ataque'
        elif distancia <= self.raio_visao:
            self.status = 'move'
        else:
            self.status = 'parado'

    def acao(self,player):
        if self.status == 'ataque':
            self.ataca_time = pygame.time.get_ticks()
            self.player_dano(self.dano)
        elif self.status == 'move':
            self.dir = self.player_distancia(player)[1]
        else:
            self.dir = pygame.math.Vector2()
        
    def cooldown(self):
        tempo = pygame.time.get_ticks()
        if not self.ataca:
            if tempo - self.ataca_time >= self.ataca_cooldown:
                self.ataca = True

        if not self.vulneravel:
            if tempo - self.hit_time >= self.invi_time:
                self.vulneravel = True

        
    def get_damage(self,player, ataque_tipo):
        if self.vulneravel:
            self.dir = self.player_distancia(player)[1]
            if ataque_tipo == 'ataque':
                self.vida -= player.cria_dano()

            self.hit_time = pygame.time.get_ticks()
            self.vulneravel = False

    def checa_morte(self):
        if self.vida <= 0:
            self.kill()
            
    def hit(self):
        if not self.vulneravel:
            self.dir *= -3

    def update(self):
        self.hit()
        self.move(self.vel)
        self.animacao()
        self.cooldown()
        self.checa_morte()

    def monstro_up(self,player):
        self.get_status(player)
        self.acao(player)
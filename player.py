import pygame, os, random


WIDTH = 800
HEIGHT = 800



# player_img = pygame.image.load(os.path.join('Graphics','player.png'))

# head sprites
hr = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_right.png'))
hu = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_up.png'))
hl = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_left.png'))
hd = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_down.png'))
# 

# body sprites
# 

# tail sprites
tr = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_right.png'))
tl = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_left.png'))
tu = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_up.png'))
td = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_down.png'))
# 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.randomize_head()
        # self.body = {
        #     "head": self.head_rect,
        #     "body": self.body,
        #     "tail": self.tail,
        # }

        self.head_img = hr
        self.body = []
        self.tail_img = tr

        self.color = (255,0,0)

        self.speedX = 10
        self.speedY = 10
        self.dir = 'r'
    
    def randomize_head(self):
        self.head_x = random.randint(0,WIDTH - 30)
        self.head_y = random.randint(0,HEIGHT - 30)
        self.head_w = 30
        self.head_h = 30
        self.head_rect  = pygame.Rect(self.head_x, self.head_y, self.head_w, self.head_h) 

    def move(self, keys):
        if keys[pygame.K_w] and self.dir != 'd':
            self.dir = 'u'
            self.change_dir()
            self.head_rect.y -= self.speedY
        elif keys[pygame.K_s] and self.dir != 'u':
            self.dir = 'd'
            self.change_dir()
            self.head_rect.y += self.speedY
        elif keys[pygame.K_a] and self.dir != 'r':
            self.dir = 'l'
            self.change_dir()
            self.head_rect.x -= self.speedX
        elif keys[pygame.K_d] and self.dir != 'l':
            self.dir = 'r'
            self.change_dir()
            self.head_rect.x += self.speedX

    

    def change_dir(self):
        if self.dir == 'r':
            self.head_img = hr
        elif self.dir == 'l':
            self.head_img = hl
        elif self.dir == 'u':
            self.head_img = hu
        elif self.dir == 'd':
            self.head_img = hd
        else: print('self.dir bug')

    def drawSelf(self, screen):
        pygame.Surface.blit(screen, self.head_img, self.head_rect )
        # pygame.draw.rect(screen, self.color, self.re ct)

    def checkCollision(self, player, enemy):
        col = pygame.sprite.collide_rect(player, enemy)
        keys = pygame.key.get_pressed()
        if col == True:
            print(col)
            print(keys)

            
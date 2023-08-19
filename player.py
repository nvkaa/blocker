import pygame, os, random


WIDTH = 900
HEIGHT = 750
BLOCK_SIZE = 30 


# player_img = pygame.image.load(os.path.join('Graphics','player.png'))

# head sprites
hr = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_right.png'))
hu = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_up.png'))
hl = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_left.png'))
hd = pygame.image.load(os.path.join('Graphics', 'snake', 'head','head_down.png'))
# 

# body sprites

bh = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_horizontal.png'))
bv = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_vertical.png'))
btl = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_tl.png'))
btl = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_tl.png'))
btl = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_tl.png'))
bbl = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_bl.png'))

# 

# tail sprites
tr = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_right.png'))
tl = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_left.png'))
tu = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_up.png'))
td = pygame.image.load(os.path.join('Graphics', 'snake', 'tail','tail_down.png'))
# 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.randomize_dir()
        self.randomize_head() 
        # print(self.dir)

        self.head_img = 0
        self.body_img = 0
        self.tail_img = 0

        self.color = (255,0,0)

        self.speedX = 10
        self.speedY = 10
        
        self.snake = [
            [
                self.tail_x, 
                self.tail_y,
                "tail", 
                self.dir,
                self.tail_img
            ], [
                self.body_x, 
                self.body_y,
                "body", 
                self.dir,
                self.body_img

            ], [
                self.head_x, 
                self.head_y,
                "head", 
                self.dir,
                self.head_img
            ]
        ]
    
    def randomize_head(self):
        self.head_x = random.randint(0,WIDTH - 90)
        self.head_y = random.randint(0,HEIGHT - 90)
        self.head_w, self.head_h = BLOCK_SIZE, BLOCK_SIZE
        self.head_rect  = pygame.Rect(self.head_x, self.head_y, self.head_w, self.head_h) 

        if self.dir == 'r':
            self.body_x = self.head_x - BLOCK_SIZE
            self.body_y = self.head_y 

            self.tail_x = self.head_x - 2*BLOCK_SIZE
            self.tail_y = self.head_y 
        elif self.dir == 'l':
            self.body_x = self.head_x + BLOCK_SIZE
            self.body_y = self.head_y 

            self.tail_x = self.head_x + 2*BLOCK_SIZE
            self.tail_y = self.head_y 
        elif self.dir == 'u':
            self.body_x = self.head_x 
            self.body_y = self.head_y + BLOCK_SIZE

            self.tail_x = self.head_x 
            self.tail_y = self.head_y + 2*BLOCK_SIZE
        elif self.dir == 'd':
            self.body_x = self.head_x 
            self.body_y = self.head_y - BLOCK_SIZE

            self.tail_x = self.head_x 
            self.tail_y = self.head_y - 2*BLOCK_SIZE

    def randomize_dir(self):
        dir = ['r', 'l', 'u', 'd']
        indx = random.randint(0, len(dir)-1)
        self.dir = dir[indx]


    def drawSelf(self, screen):
        # pygame.Surface.blit(screen, self.head_img, self.head_rect )
        # pygame.draw.rect(screen, self.color, self.re ct)

        sprite_list = []
        for part in self.snake:
            if part[2] == "head":
                if part[3] == "u":
                    self.head_img = hu
                    part[4] = hu
                    sprite_list.append(part)

                if part[3] == "d":
                    self.head_img = hd
                    part[4] = hd
                    sprite_list.append(part)

                if part[3] == "l":
                    self.head_img = hl
                    part[4] = hl
                    sprite_list.append(part)
                    
                if part[3] == "r":
                    self.head_img = hr
                    part[4] = hr
                    sprite_list.append(part)

            if part[2] == "body":
                if part[3] == "u":
                    self.body_img = bv
                    part[4] = bv
                    sprite_list.append(part)

                if part[3] == "d":
                    self.body_img  = bv
                    part[4] = bv
                    sprite_list.append(part)
                    
                if part[3] == "l":
                    self.body_img  = bh
                    part[4] = bh
                    sprite_list.append(part)
                    
                if part[3] == "r":
                    self.body_img  = bh
                    part[4] = bh
                    sprite_list.append(part)
                    
            if part[2] == "tail":
                if part[3] == "u":
                    self.tail_img = td
                    part[4] = td
                    sprite_list.append(part)

                if part[3] == "d":                    
                    self.tail_img = tu
                    part[4] = tu
                    sprite_list.append(part)

                if part[3] == "l":
                    self.tail_img = tr
                    part[4] = tr
                    sprite_list.append(part)
                    
                if part[3] == "r":
                    self.tail_img = tl   
                    part[4] = tl
                    sprite_list.append(part)
            # else: print('bugged') 
            # print(sprite_list)

            # if part[3] == "up":
            #     self.dir = 'u'
            # if part[3] == "down":
            #     self.dir = 'd'
            # if part[3] == "left":
            #     self.dir = 'l'
            # if part[3] == "right ":
            #     self.dir = 'r'

        for part in sprite_list:
            pygame.Surface.blit(screen, part[4], (part[0], part[1]))

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
            # self.body_img = 
        elif self.dir == 'l':
            self.head_img = hl
        elif self.dir == 'u':
            self.head_img = hu
        elif self.dir == 'd':
            self.head_img = hd
        else: print('self.dir bug')

    

    def checkCollision(self, player, enemy):
        col = pygame.sprite.collide_rect(player, enemy)
        keys = pygame.key.get_pressed()
        if col == True:
            print(col)
            print(keys)

            
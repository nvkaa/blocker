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
btr = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_tr.png'))
bbr = pygame.image.load(os.path.join('Graphics', 'snake', 'body','body_br.png'))
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
        self.speedX = 0
        self.speedY = 0
        # print(self.dir)

        self.head_img = None
        self.body_img = None
        self.tail_img = None

        self.color = (255,0,0)

        
        self.randomize_dir()
        self.randomize_head() 

    def randomize_dir(self):
        # dir = ['r', 'l', 'u', 'd']
        # indx = random.randint(0, len(dir)-1)
        # self.dir = dir[indx]
        self.dir = 'r'
     
    
    def randomize_head(self):        
        self.head_x = random.randint(90,WIDTH - 90)
        self.head_y = random.randint(90,HEIGHT - 90) 
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

        # headx, heady = self.head_x, self.head_y

        bodyx, bodyy = self.body_x, self.body_y

        tailx, taily = self.tail_x, self.tail_y

        self.snake = [
            [
                tailx, 
                taily,
                "tail", 
                self.dir,
                self.tail_img,
            ], [
                bodyx, 
                bodyy,
                "body", 
                self.dir,
                self.body_img

            ], [
                self.head_x, 
                self.head_y,
                "head", 
                self.dir,
                self.head_img,
                # self.speedX,
                # self.speedY
            ]
        ]



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


            



        for part in sprite_list:
            pygame.Surface.blit(screen, part[4], (part[0], part[1]))

    def move(self, keys):
        tp = self.snake
        for part in self.snake:
            if keys == pygame.K_UP and part[3] != 'd':
                self.snake[-1][3] = 'u'
                self.speedY = 10
                self.speedX = 0
                self.snake[-1][1] -= self.speedY

                if part[3] == 'u':
                    for block in self.snake[:-1]:
                        self.speedY = 10
                        self.speedX = 0
                        block[1] -= self.speedY
                    
                elif part[3] == 'r':
                    for block in self.snake[:-1]:
                        if block[0] < tp[-1][0]:
                            self.snake[-2][4] = btl
                            self.speedX = 10
                            block[0] += self.speedX
                        else: 
                            self.speedX = 0
                            self.speedY = 10
                            block[1] -= self.speedY
                            block[3] = 'u'
                elif part[3] == 'l':
                    if block[0] > tp[-1][0]:
                        self.snake[-2][4] = btr
                        self.speedX = 10
                        block[0] -= self.speedX
                    else: 
                        self.speedX = 0
                        self.speedY = 10
                        block[1] -= self.speedY
                        block[3] = 'u'
            
            elif keys == pygame.K_DOWN and part[3] != 'u':
                self.snake[-1][3] = 'd'
                self.speedY = 10
                self.speedX = 0
                self.snake[-1][1] += self.speedY

                if part[3] == 'd':
                    for block in self.snake[:-1]:
                        self.speedY = 10
                        self.speedX = 0
                        block[1] += self.speedY
                    
                elif part[3] == 'r':
                    for block in self.snake[:-1]:
                        if block[0] < tp[-1][0]:
                            self.snake[-2][4] = bbl
                            self.speedX = 10
                            block[0] += self.speedX
                        else: 
                            self.speedX = 0
                            self.speedY = 10
                            block[1] += self.speedY
                            block[3] = 'd'
                
                elif part[3] == 'l':
                    if block[0] > tp[-1][0]:
                        self.snake[-2][4] = bbl
                        self.speedX = 10
                        block[0] -= self.speedX
                    else: 
                        self.speedX = 0
                        self.speedY = 10
                        block[1] += self.speedY
                        block[3] = 'u'

            if keys == pygame.K_LEFT and part[3] != 'r':
                self.snake[-1][3] = 'l'
                self.speedY = 0
                self.speedX = 10
                self.snake[-1][0] -= self.speedX

                if part[3] == 'l':
                    for block in self.snake[:-1]:
                        self.speedY = 0
                        self.speedX = 10
                        block[0] -= self.speedX
                    
                elif part[3] == 'u':
                    for block in self.snake[:-1]:
                        if block[1] > tp[-1][1]:
                            self.snake[-2][4] = bbl
                            self.speedY = 10
                            block[1] -= self.speedY
                        else: 
                            self.speedX = 10
                            self.speedY = 0
                            block[0] -= self.speedX
                            block[3] = 'l'

                elif part[3] == 'd':
                    if block[1] < tp[-1][1]:
                        self.snake[-2][4] = btl
                        self.speedX = 10
                        block[0] -= self.speedX
                    else: 
                        self.speedX = 10
                        self.speedY = 0
                        block[0] -= self.speedX
                        block[3] = 'l'

            if keys == pygame.K_RIGHT and part[3] != 'l':
                self.snake[-1][3] = 'r'
                self.speedY = 0
                self.speedX = 10
                self.snake[-1][0] += self.speedX

                if part[3] == 'r':
                    for block in self.snake[:-1]:
                        self.speedY = 0
                        self.speedX = 10
                        block[0] += self.speedX
                    
                elif part[3] == 'u':
                    for block in self.snake[:-1]:
                        if block[1] > tp[-1][1]:
                            self.snake[-2][4] = bbr
                            self.speedY = 10
                            block[0] -= self.speedY
                        else: 
                            self.speedX = 10
                            self.speedY = 0
                            block[1] += self.speedX
                            block[3] = 'r'
                        



    def change_dir(self, t_p):
        for part in t_p:
            if part[2] == 'r' and self.dir == 'u':
                pass

        # if self.dir == 'r':
        #     self.head_img = hr
        #     # self.body_img = 
        # elif self.dir == 'l':
        #     self.head_img = hl
        # elif self.dir == 'u':
        #     self.head_img = hu
        # elif self.dir == 'd':
        #     self.head_img = hd
        # else: print('self.dir bug')

    def checkCollision(self, player, enemy):
        col = pygame.sprite.collide_rect(player, enemy)
        keys = pygame.key.get_pressed()
        if col == True:
            print(col)
            print(keys)

            
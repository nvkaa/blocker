import pygame
import os


enemy_img = pygame.image.load(os.path.join('Graphics','enemy.png'))
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = enemy_img
        self.color = (255,0,0)
        self.speed = 10
    def move(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    def drawSelf(self, screen):
        pygame.Surface.blit(screen, self.image, self.rect)
    
        

# Example file showing a basic pygame "game loop"
import pygame
from player import *
from enemy import Enemy

# pygame setup
pygame.init()



screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
##myWindow = pygame.Surface((1024, 720)).convert()
# screen.fill("purple")
clock = pygame.time.Clock()


dt = 0
##player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

CAT_UPDATE = pygame.USEREVENT
pygame.time.set_timer(CAT_UPDATE, 150) 	
def main():
    player = Player()
    # player.randomize_head()
    # player.randomize_dir()
    # enemy = Enemy(200,200,50,50)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()



        
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        # enemy.move(keys)

        screen.fill("purple")
        player.drawSelf(screen)
        # enemy.drawSelf(screen)
        # player.checkCollision(player, enemy)

        # flip() the display to put your work on screen
        pygame.display.flip()

        #clock.tick(60)  # limits FPS to 60
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

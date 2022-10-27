import pygame
import sys
import graph
ROW=35
SIZE=556
TILE=17
class PacMan(pygame.sprite.Sprite):
    def __init__(self,w,h,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load("pacman.png")
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.x, self.y = pos_x, pos_y

    def move_to(self, x, y):
        self.x, self.y = x, y

    

def draw(window, size, rows):
    distance_between_rows = size // rows
    x=0
    y=0
    for i in range(rows):
        x+= distance_between_rows
        y+= distance_between_rows
        pygame.draw.line(window,(0,0,0),(x,0),(x,size))
        pygame.draw.line(window,(0,0,0),(0,y),(size,y))
# def get_rect(x, y):
#     return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2

# #Grid
# grid = [[1 for col in range(ROW)] for row in range(ROW)]

def main():
    screen = pygame.display.set_mode((SIZE,SIZE))
    pygame.display.set_caption("Pac Man")

    maze = pygame.image.load("maze.png").convert()

    maze_rect= maze.get_rect(topleft=(0,0))
    myPacMan = PacMan(20,20,535,535)

    pacman_group=pygame.sprite.Group()
    pacman_group.add(myPacMan)
    
    while True:
        screen.blit(maze,maze_rect)
        draw(screen,SIZE,ROW)
        # [[pygame.draw.rect(screen, pygame.Color('darkorange'), get_rect(x, y), border_radius=TILE // 5)
        #     for x, col in enumerate(row) if col] for y, row in enumerate(grid)]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pacman_group.draw(screen)
        pygame.display.update()

    

if __name__=="__main__":
    main()